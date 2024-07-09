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

class SimpleController(Node):
    def __init__(self):
        super().__init__("wheel_controller")
        self.declare_parameter("wheel_radius", 0.0875)
        self.declare_parameter("wheel_separation", 0.657)
        self.declare_parameter("max_acceleration", 0.2)  # Potentially adjust this based on hardware limits
        self.declare_parameter("max_speed", 1.5)  # Robot linear speed

        self.wheel_radius = self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_separation = self.get_parameter("wheel_separation").get_parameter_value().double_value
        self.max_acceleration = self.get_parameter("max_acceleration").get_parameter_value().double_value
        self.max_speed = self.get_parameter("max_speed").get_parameter_value().double_value
        self.publisher_L = self.create_publisher(COData, '/motorL/tpdo', 10)
        self.publisher_R = self.create_publisher(COData, '/motorR/tpdo', 10)
        self.wheel_speed_pub = self.create_publisher(Float64MultiArray, 'wheel_speeds', 60)
        self.traveled_distance_pub = self.create_publisher(Float64, 'traveled_dist', 60)

        self.current_wheel_speed = np.array([0.0, 0.0])
        self.target_distance = 0.0
        self.target_angle = 0.0
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0

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

    def update_movement(self, response):
        if self.moving:
            current_time = self.get_clock().now()
            dt = (current_time - self.last_time).nanoseconds / 1e9
            self.last_time = current_time

            remaining_distance = self.target_distance - self.traveled_distance
            remaining_angle = self.target_angle - self.traveled_angle

            # Determine the phase of motion based on the portion of the distance traveled
            phase_distance = 0.1 * abs(self.target_distance)  # Reduced the acceleration phase distance
            is_accelerating = abs(self.traveled_distance) < phase_distance and abs(self.traveled_distance) / phase_distance < 1
            is_decelerating = abs(remaining_distance) < phase_distance and abs(remaining_distance) / phase_distance < 1

            # Debug output
            self.get_logger().info(f"Acceleration: {is_accelerating}, Deceleration: {is_decelerating}, Linear speed: {self.max_speed}, DT: {dt} , RD: {remaining_distance}" )

            # Sinusoidal speed profiles for smoother transitions
            if is_accelerating:
                accel_factor = math.sin((math.pi / 2) * (abs(self.traveled_distance) / phase_distance))
                linear_speed = accel_factor * self.max_speed * np.sign(self.target_distance)
                angular_speed = accel_factor * (self.max_speed / self.wheel_separation) * np.sign(self.target_angle)
            elif is_decelerating:
                decel_factor = math.sin((math.pi / 2) * (abs(remaining_distance) / phase_distance))
                linear_speed = decel_factor * self.max_speed * np.sign(self.target_distance)
                angular_speed = decel_factor * (self.max_speed / self.wheel_separation) * np.sign(self.target_angle)
            else:
                linear_speed = self.max_speed * np.sign(self.target_distance)
                angular_speed = self.max_speed / self.wheel_separation * np.sign(self.target_angle)

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

            # Convert to motor commands and publish
            self.publish_wheel_speeds()

            if abs(remaining_distance) < 0.01 and abs(remaining_angle) < 0.01:
                self.current_wheel_speed = np.array([0.0, 0.0])
                response.success = True
                self.moving = False
                self.get_logger().info("Movement stopped. Target reached.")
                return  # Stop the update cycle

            # Continue updating if still moving
            timer_period = 0.1  # Adjust as necessary
            self.timer = self.create_timer(timer_period, lambda: self.update_movement(response))

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
