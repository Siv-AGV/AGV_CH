#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from agv_msgs.srv import Move
import numpy as np
import math
from canopen_interfaces.msg import COData
import time

class SimpleController(Node):
    def __init__(self):
        super().__init__("wheel_controller")
        self.declare_parameter("wheel_radius", 0.0875)
        self.declare_parameter("wheel_separation", 0.657)
        self.declare_parameter("max_acceleration", 0.2)  # User-provided max acceleration
        self.declare_parameter("max_speed", 1.5)  # User-provided max speed

        self.wheel_radius = self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_separation = self.get_parameter("wheel_separation").get_parameter_value().double_value
        self.max_acceleration = self.get_parameter("max_acceleration").get_parameter_value().double_value
        self.max_speed = self.get_parameter("max_speed").get_parameter_value().double_value
        self.publisher_L = self.create_publisher(COData, '/motorL/tpdo', 10)
        self.publisher_R = self.create_publisher(COData, '/motorR/tpdo', 10)
        self.publisher_L_Dir = self.create_publisher(COData, '/motorL/tpdo', 10)
        self.publisher_R_Dir = self.create_publisher(COData, '/motorR/tpdo', 10)
        self.wheel_speed_pub = self.create_publisher(Float64MultiArray, 'wheel_speeds', 60)
        self.traveled_distance_pub = self.create_publisher(Float64, 'traveled_dist', 60)

        self.current_wheel_speed = np.array([0.0, 0.0])
        self.target_distance = 0.0
        self.target_angle = 0.0
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0
        self.count = 0

        self.last_time = None
        self.moving = False

        self.speed_conversion = np.array([[self.wheel_radius / 2, self.wheel_radius / 2],
                                          [self.wheel_radius / self.wheel_separation, -self.wheel_radius / self.wheel_separation]])

        self.service = self.create_service(Move, "wheel_control_service", self.command_callback)
        self.get_logger().info("Service is ready.")

    def command_callback(self, request, response):
        if not self.moving:  # Ensure it doesn't handle new requests if already moving
            msg = request.command
            self.target_distance = msg.linear.x
            self.target_angle = msg.angular.z

            self.traveled_distance = 0.0
            self.traveled_angle = 0.0

            self.last_time = self.get_clock().now()
            self.moving = True
            self.update_movement(response)

        return response

    def trapezoidal_velocity_profile(self, distance, max_speed, max_acceleration, traveled_distance):
        if distance == 0:
            return 0.0

        t_acc = max_speed / max_acceleration
        d_acc = 0.5 * max_acceleration * t_acc**2

        if distance < 2 * d_acc:
            v_peak = np.sqrt(max_acceleration * distance)
            t_acc = v_peak / max_acceleration
            d_acc = 0.5 * max_acceleration * t_acc**2

        if traveled_distance < d_acc:
            velocity = np.sqrt(2 * max_acceleration * traveled_distance)
        elif traveled_distance < distance - d_acc:
            velocity = max_speed
        else:
            velocity = np.sqrt(2 * max_acceleration * (distance - traveled_distance))

        return velocity
    
    
    
    def decimal_to_hex(decimal_value, bit_length=32):
        if decimal_value >= 0:
            # Positive decimal
            return hex(decimal_value)
        else:
            # Negative decimal, use two's complement
            two_complement_value = (1 << bit_length) + decimal_value
            return hex(two_complement_value)

    def update_movement(self, response):
        if self.moving:
            current_time = self.get_clock().now()
            dt = (current_time - self.last_time).nanoseconds / 1e9
            self.last_time = current_time

            remaining_distance = self.target_distance - self.traveled_distance
            remaining_angle = self.target_angle - self.traveled_angle

            linear_speed = self.trapezoidal_velocity_profile(abs(self.target_distance), self.max_speed, self.max_acceleration, abs(self.traveled_distance)) * np.sign(self.target_distance)
            angular_speed = self.trapezoidal_velocity_profile(abs(self.target_angle), self.max_speed / self.wheel_separation, self.max_acceleration, abs(self.traveled_angle)) * np.sign(self.target_angle)

            # Ensure linear and angular speeds are not set to zero prematurely
            if abs(linear_speed) < 0.001:
                linear_speed = np.sign(self.target_distance) * 0.001
            if abs(angular_speed) < 0.001:
                angular_speed = np.sign(self.target_angle) * 0.001

            # Update odometry
            self.traveled_distance += linear_speed * dt
            self.traveled_angle += angular_speed * dt

            # Compute individual wheel speeds from linear and angular velocities
            agv_speed = np.array([[linear_speed], [angular_speed]])
            self.wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion), agv_speed)

            self.current_wheel_speed_conv_L = int(np.nan_to_num(((self.wheel_speed[0] / (2 * math.pi)) * 60 * 20 * 512 * 10000) / 1875))
            self.current_wheel_speed_conv_R = int(np.nan_to_num(((self.wheel_speed[1] / (2 * math.pi)) * 60 * 20 * 512 * 10000) / 1875))  # negative because the motor is inverted
            # self.current_wheel_speed_conv_L_s = int(np.nan_to_num(((self.wheel_speed[0] / (2 * math.pi)) * 60 * 20 * 512 * 10000) / 1875))
            # self.current_wheel_speed_conv_R_s = int(np.nan_to_num(((self.wheel_speed[1] / (2 * math.pi)) * 60 * 20 * 512 * 10000) / 1875))
            self.current_wheel_speed_conv_L_hex = decimal_to_hex(self.current_wheel_speed_conv_L_hex)
            self.current_wheel_speed_conv_R_hex = decimal_to_hex(self.current_wheel_speed_conv_L_hex)


           # Convert to motor commands and publish
            self.publish_wheel_speeds()

            # if self.count < 1:
            #     self.publish_wheel_speed_L_Direction()
            #     self.publish_wheel_speed_R_Direction()
            #     self.count += 1
            # else:
            #     self.publish_wheel_speed_L()
            #     self.publish_wheel_speed_R()

            if abs(remaining_distance) < 0.01 and abs(remaining_angle) < 0.01:
                self.current_wheel_speed = np.array([0.0, 0.0])
                response.success = True
                self.moving = False
                self.current_wheel_speed_conv_L = 0
                self.current_wheel_speed_conv_R = 0
                self.current_wheel_speed_conv_L_s = 0
                self.current_wheel_speed_conv_R_s = 0
                self.publish_wheel_speed_L()
                self.publish_wheel_speed_R()
                self.get_logger().info("Movement stopped. Target reached.")
                self.count = 0

                return  # Stop the update cycle

            # Continue updating if still moving
            timer_period = 0.1  # Adjust as necessary
            self.timer = self.create_timer(timer_period, lambda: self.update_movement(response))
            self.get_logger().info(f"Linear speed: {linear_speed}, Angular speed: {angular_speed}, DT: {dt}, RD: {remaining_distance}")

    # def publish_wheel_speed_L_Direction(self):
    #     msg = COData()
    #     msg.index = 0x607E
    #     msg.subindex = 0
    #     msg.data = 0 if self.current_wheel_speed_conv_L_s < 0 else 1
    #     self.publisher_L_Dir.publish(msg)

    # def publish_wheel_speed_R_Direction(self):
    #     msg = COData()
    #     msg.index = 0x607E
    #     msg.subindex = 0
    #     msg.data = 0 if self.current_wheel_speed_conv_R_s < 0 else 1
    #     self.publisher_R_Dir.publish(msg)

    def publish_wheel_speed_L(self):
        msg = COData()
        msg.index = 0x60FF
        msg.subindex = 0
        msg.data = self.current_wheel_speed_conv_L_hex
        self.publisher_L.publish(msg)
       
    def publish_wheel_speed_R(self):
        msg = COData()
        msg.index = 0x60FF
        msg.subindex = 0
        msg.data = self.current_wheel_speed_conv_R_hex
        self.publisher_R.publish(msg)
        

   

    def publish_wheel_speeds(self):
        wheel_speed_msg = Float64MultiArray()
        wheel_speed_msg.data = [self.wheel_speed[0, 0], self.wheel_speed[1, 0]]
        self.wheel_speed_pub.publish(wheel_speed_msg)
        traveled_distance_msg = Float64()
        traveled_distance_msg.data = self.traveled_distance
        self.wheel_speed_pub.publish(wheel_speed_msg)
        self.traveled_distance_pub.publish(traveled_distance_msg)

def main(args=None):
    rclpy.init()
    simple_controller = SimpleController()
    rclpy.spin(simple_controller)
    simple_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
