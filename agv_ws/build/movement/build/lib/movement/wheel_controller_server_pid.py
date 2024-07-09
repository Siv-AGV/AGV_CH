#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Twist
from agv_msgs.srv import Move
import numpy as np
import math
from simple_pid import PID

class AGVController(Node):
    def __init__(self):
        super().__init__("wheel_controller_pid")
        # Declare and get parameters
        # self.declare_parameters()
        # self.get_parameters()

        self.declare_parameter("wheel_radius", 0.0875)
        self.declare_parameter("wheel_separation", 0.657)
        self.declare_parameter("max_acceleration", 0.1)
        self.declare_parameter("max_speed", 1.5)
        self.declare_parameter("kp_linear", 1.0)
        self.declare_parameter("ki_linear", 0.1)
        self.declare_parameter("kd_linear", 0.05)
        self.declare_parameter("kp_angular", 0.8)
        self.declare_parameter("ki_angular", 0.05)
        self.declare_parameter("kd_angular", 0.03)

        self.wheel_radius = self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_separation = self.get_parameter("wheel_separation").get_parameter_value().double_value
        self.max_acceleration = self.get_parameter("max_acceleration").get_parameter_value().double_value
        self.max_speed = self.get_parameter("max_speed").get_parameter_value().double_value
        self.kp_linear = self.get_parameter("kp_linear").get_parameter_value().double_value
        self.ki_linear = self.get_parameter("ki_linear").get_parameter_value().double_value
        self.kd_linear = self.get_parameter("kd_linear").get_parameter_value().double_value
        self.kp_angular = self.get_parameter("kp_angular").get_parameter_value().double_value
        self.ki_angular = self.get_parameter("ki_angular").get_parameter_value().double_value
        self.kd_angular = self.get_parameter("kd_angular").get_parameter_value().double_value

        # Publishers
        self.publisher_L = self.create_publisher(Float64MultiArray, '/motorL/tpdo', 10)
        self.publisher_R = self.create_publisher(Float64MultiArray, '/motorR/tpdo', 10)

        self.wheel_speed_pub = self.create_publisher(Float64MultiArray, 'wheel_speeds', 10)

        # State variables
        self.init_state_vars()

        # PID Controllers
        self.pid_linear = PID(self.kp_linear, self.ki_linear, self.kd_linear, setpoint=0)
        self.pid_angular = PID(self.kp_angular, self.ki_angular, self.kd_angular, setpoint=0)

        # Conversion matrix for wheel speeds
        self.setup_conversion_matrix()

        # Service
        self.service = self.create_service(Move, "wheel_control_service", self.command_callback)
        self.get_logger().info("AGV Controller is ready.")

        

    def init_state_vars(self):
        self.current_wheel_speed = np.array([0.0, 0.0])
        self.target_distance = 0.0
        self.target_angle = 0.0
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0
        self.last_time = None
        self.moving = False

    def setup_conversion_matrix(self):
        self.speed_conversion = np.array([
            [self.wheel_radius / 2, self.wheel_radius / 2],
            [self.wheel_radius / self.wheel_separation, -self.wheel_radius / self.wheel_separation]
        ])

    def command_callback(self, request, response):
        if not self.moving:  # Handle new requests if not already moving
            msg = request.command
            self.target_distance = msg.linear.x
            self.target_angle = msg.angular.z
            self.reset_movement()
            self.last_time = self.get_clock().now()
            self.moving = True
            self.update_movement(response)
        return response

    def reset_movement(self):
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0
        self.pid_linear.setpoint = self.target_distance
        self.pid_angular.setpoint = self.target_angle

    def update_movement(self, response):
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        remaining_distance = self.pid_linear(self.traveled_distance)
        remaining_angle = self.pid_angular(self.traveled_angle)
        linear_speed = max(min(self.max_speed, remaining_distance / dt), -self.max_speed)
        angular_speed = max(min(self.max_speed / self.wheel_separation, remaining_angle / dt), -self.max_speed / self.wheel_separation)

        # Update traveled distance and angle based on the calculated speeds
        self.traveled_distance += linear_speed * dt
        self.traveled_angle += angular_speed * dt

        # Compute wheel speeds from AGV speeds
        wheel_speeds = np.matmul(self.speed_conversion, np.array([linear_speed, angular_speed]))

        # Limit wheel speed changes to prevent abrupt jumps
        self.current_wheel_speed = np.clip(wheel_speeds, self.current_wheel_speed - self.max_acceleration * dt,
                                           self.current_wheel_speed + self.max_acceleration * dt)

        # Publish wheel speeds
        self.publish_wheel_speeds()

        # Check if the target is reached
        if abs(self.target_distance - self.traveled_distance) < 0.01 and abs(self.target_angle - self.traveled_angle) < 0.01:
            self.moving = False
            response.success = True
            self.stop_movement()
            return

        # Continue updating movement if not reached
        self.timer = self.create_timer(0.05, lambda: self.update_movement(response))

    def publish_wheel_speeds(self):
        msg = Float64MultiArray()
        msg.data = self.current_wheel_speed.tolist()
        self.wheel_speed_pub.publish(msg)

    def stop_movement(self):
        # Reset wheel speeds to zero
        self.current_wheel_speed = np.array([0.0, 0.0])
        self.publish_wheel_speeds()
        self.get_logger().info("Movement stopped. Target reached.")

def main(args=None):
    rclpy.init()
    agv_controller = AGVController()
    rclpy.spin(agv_controller)
    agv_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
