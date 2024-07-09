#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray, Float64
from geometry_msgs.msg import Twist
from agv_msgs.srv import Move
import numpy as np
import math
from canopen_interfaces.msg import COData

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
        self.wheel_speed_pub = self.create_publisher(Float64MultiArray, 'wheel_speeds', 10)
        self.traveled_distance_pub = self.create_publisher(Float64, 'traveled_dist', 10)
        self.remaining_distance_pub = self.create_publisher(Float64, 'remaining_dist', 10)
        self.angular_speed_pub = self.create_publisher(Float64, 'agv_angular_speed', 10)

        self.current_wheel_speed = np.array([0.0, 0.0])
        self.target_distance = 0.0
        self.target_angle = 0.0
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0
        self.traveled_distance_local = 0.0
        self.traveled_distance_old = 0.0
        self.traveled_angle_local = 0.0
        self.traveled_angle_old = 0.0

        self.last_time = None
        self.moving = False

        self.speed_conversion = np.array([[self.wheel_radius / 2, self.wheel_radius / 2],
                                          [self.wheel_radius / self.wheel_separation, -self.wheel_radius / self.wheel_separation]])

        self.service = self.create_service(Move, "wheel_control_service", self.command_callback)
        self.timer = self.create_timer(0.02, self.update_movement)  # Create timer once
        self.timer.cancel()  # Start with the timer canceled
        self.get_logger().info("Service is ready.")

        # Subscribe to the QR Input node for PGV corrections
        self.pgv_subscriber = self.create_subscription(Float64MultiArray, 'pgv_converted', self.pgv_callback, 10)
        self.correction_data = [0.0, 0.0, 0.0]

    def command_callback(self, request, response):
        if not self.moving:  # Ensure it doesn't handle new requests if already moving
            msg = request.command

            # Preserve the sign of the distance
            self.target_distance = msg.linear.x
            self.target_angle = msg.angular.z

            self.traveled_distance = 0.0
            self.traveled_angle = 0.0

            self.last_time = self.get_clock().now()
            self.moving = True
            self.timer.reset()  # Reset and start the timer

        return response

    def trapezoidal_velocity_profile(self, distance, max_speed, max_acceleration, traveled_distance):
        if distance == 0:
            return 0.0

        t_acc = max_speed / max_acceleration
        d_acc = 0.5 * max_acceleration * t_acc**2

        if abs(distance) < 2 * d_acc:
            v_peak = np.sqrt(max_acceleration * abs(distance))
            t_acc = v_peak / max_acceleration
            d_acc = 0.5 * max_acceleration * t_acc**2

        if abs(traveled_distance) < d_acc:
            velocity = np.sqrt(2 * max_acceleration * abs(traveled_distance))
        elif abs(traveled_distance) < abs(distance) - d_acc:
            velocity = max_speed
        else:
            velocity = np.sqrt(2 * max_acceleration * (abs(distance) - abs(traveled_distance)))

        return velocity

    def decimal_to_hex(self, decimal_value, bit_length=32):
        if decimal_value >= 0:
            return int(decimal_value)
        else:
            two_complement_value = (1 << bit_length) + decimal_value
            return int(two_complement_value)

    def pgv_callback(self, msg):
        self.correction_data = msg.data

    def apply_corrections(self):
        x_position, y_position, angle = self.correction_data
        distance_correction = np.sqrt(x_position**2 + y_position**2)
        angle_correction = math.atan2(y_position, 1.0) + angle

        # Update the target distance and angle with corrections
        self.target_distance += -distance_correction
        self.target_angle += -angle_correction

        self.get_logger().info(f"Corrections applied: Distance correction: {distance_correction}, Angle correction: {angle_correction}")

        # Reset correction data
        self.correction_data = [0.0, 0.0, 0.0]

    def update_movement(self):
        if self.moving:
            current_time = self.get_clock().now()
            dt = (current_time - self.last_time).nanoseconds / 1e9
            self.last_time = current_time

            remaining_distance = self.target_distance - self.traveled_distance
            remaining_angle = self.target_angle - self.traveled_angle

            # Calculate linear and angular speeds
            if abs(remaining_angle) > 0.001:
                angular_speed = self.trapezoidal_velocity_profile(self.target_angle, self.max_speed / self.wheel_separation, self.max_acceleration, self.traveled_angle) * np.sign(self.target_angle)
            else:
                angular_speed = 0.0

            if abs(remaining_distance) > 0.001:
                linear_speed = self.trapezoidal_velocity_profile(self.target_distance, self.max_speed, self.max_acceleration, self.traveled_distance) * np.sign(self.target_distance)
            else:
                linear_speed = 0.0

            # Apply minimum threshold to avoid stalling
            if abs(linear_speed) < 0.001 and remaining_distance != 0:
                linear_speed = np.sign(remaining_distance) * 0.001
            if abs(angular_speed) < 0.001 and remaining_angle != 0:
                angular_speed = np.sign(remaining_angle) * 0.001

            angular_speed_msg = Float64()
            angular_speed_msg.data = angular_speed
            self.angular_speed_pub.publish(angular_speed_msg)

            # Update traveled distance and angle
            self.traveled_distance += linear_speed * dt
            self.traveled_angle += angular_speed * dt

            # Apply corrections every 1.5 meters of travel and after rotation
            self.traveled_distance_local = self.traveled_distance - self.traveled_distance_old

            # Apply corrections if available
            if abs(self.traveled_distance_local) >= 1.5 and abs(remaining_distance) >= 1.0:
                self.apply_corrections()
                self.traveled_distance_local = 0.0
                self.traveled_distance_old = self.traveled_distance
                self.get_logger().info("Applied corrections based on PGV data")

            # Calculate wheel speeds
            agv_speed = np.array([[linear_speed], [angular_speed]])
            self.wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion), agv_speed)

            # Convert wheel speed to the motor's speed units and apply necessary scaling
            self.current_wheel_speed_conv_L = int(np.nan_to_num(((self.wheel_speed[0] / (2 * math.pi)) * 60 * 20 * 512 * 10000) / 1875))
            self.current_wheel_speed_conv_R = -int(np.nan_to_num(((self.wheel_speed[1] / (2 * math.pi)) * 60 * 20 * 512 * 10000) / 1875))
            self.current_wheel_speed_conv_L_hex = self.decimal_to_hex(self.current_wheel_speed_conv_L)
            self.current_wheel_speed_conv_R_hex = self.decimal_to_hex(self.current_wheel_speed_conv_R)

            self.publish_wheel_speeds()
            self.publish_wheel_speed_L()
            self.publish_wheel_speed_R()

            remaining_distance_msg = Float64()
            remaining_distance_msg.data = remaining_distance
            self.remaining_distance_pub.publish(remaining_distance_msg)

            self.get_logger().info(f"Linear speed: {linear_speed}, Angular speed: {angular_speed}, DT: {self.traveled_distance}, RD: {remaining_distance}")

            # Check if both linear and angular targets are reached
            if abs(remaining_distance) < 0.005 and abs(remaining_angle) < 0.002:
                self.current_wheel_speed = np.array([0.0, 0.0])
                self.moving = False
                self.timer.cancel()
                self.current_wheel_speed_conv_L = 0
                self.current_wheel_speed_conv_R = 0
                self.current_wheel_speed_conv_L_hex = 0
                self.current_wheel_speed_conv_R_hex = 0
                self.publish_wheel_speed_L()
                self.publish_wheel_speed_R()
                angular_speed = 0.0
                angular_speed_msg = Float64()
                angular_speed_msg.data = 0.0
                self.angular_speed_pub.publish(angular_speed_msg)
                self.get_logger().info("Movement stopped. Target reached.")
                self.traveled_distance_old = 0.0
                self.get_logger().info(f"Linear speed: {linear_speed}, Angular speed: {angular_speed}, DT: {self.traveled_distance}, RD: {remaining_distance}")

    def publish_wheel_speed_L(self):
        msg0 = COData()
        msg0.index = 0x60FF
        msg0.subindex = 0
        msg0.data = self.current_wheel_speed_conv_L_hex
        self.publisher_L.publish(msg0)

    def publish_wheel_speed_R(self):
        msg1 = COData()
        msg1.index = 0x60FF
        msg1.subindex = 0
        msg1.data = self.current_wheel_speed_conv_R_hex
        self.publisher_R.publish(msg1)

    def publish_wheel_speeds(self):
        wheel_speed_msg = Float64MultiArray()
        wheel_speed_msg.data = [self.wheel_speed[0, 0], self.wheel_speed[1, 0]]
        self.wheel_speed_pub.publish(wheel_speed_msg)
        traveled_distance_msg = Float64()
        traveled_distance_msg.data = self.traveled_distance
        self.traveled_distance_pub.publish(traveled_distance_msg)

def main(args=None):
    rclpy.init()
    simple_controller = SimpleController()
    rclpy.spin(simple_controller)
    simple_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
