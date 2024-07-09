#!/usr/bin/env python3
import rclpy
from rclpy.lifecycle import LifecycleNode
from rclpy.lifecycle import LifecycleState
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Twist
import numpy as np

class WheelController(LifecycleNode):
    def __init__(self):
        super().__init__("wheel_controller")
        self.declare_parameter("wheel_radius", 0.0875)
        self.declare_parameter("wheel_separation", 0.657)
        self.declare_parameter("max_acceleration", 0.1)
        self.declare_parameter("max_speed", 0.2)  # Max linear speed

        self.wheel_radius = self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_separation = self.get_parameter("wheel_separation").get_parameter_value().double_value
        self.max_acceleration = self.get_parameter("max_acceleration").get_parameter_value().double_value
        self.max_speed = self.get_parameter("max_speed").get_parameter_value().double_value

        self.current_wheel_speed = np.array([0.0, 0.0])
        self.target_distance = 0.0
        self.target_angle = 0.0
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0

        self.last_time = None
        self.wheel_cmd_pub = None 
        self.vel_sub = self.create_subscription(Twist, "command_topic", self.vel_callback, 10)

    def on_configure(self, state):
        self.get_logger().info("Configuring WheelController node...")
        self.wheel_cmd_pub = self.create_publisher(Float64MultiArray, "wheel_velocity_commands", 10)
        self.last_time = self.get_clock().now()
        return LifecycleState.SUCCESS

    def on_activate(self, state):
        self.get_logger().info("Activating WheelController node...")
        return LifecycleState.SUCCESS

    def on_deactivate(self, state):
        self.get_logger().info("Deactivating WheelController node...")
        return LifecycleState.SUCCESS

    def on_cleanup(self, state):
        self.get_logger().info("Cleaning up WheelController node...")
        return LifecycleState.SUCCESS

    def vel_callback(self, msg):
        self.target_distance = msg.linear.x
        self.target_angle = msg.angular.z

        self.traveled_distance = 0.0
        self.traveled_angle = 0.0

        if hasattr(self, 'timer'):
            self.timer.cancel()

        self.last_time = self.get_clock().now()
        self.update_movement()

    def update_movement(self):
        if not self.last_time:
            return

        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        remaining_distance = self.target_distance - self.traveled_distance
        remaining_angle = self.target_angle - self.traveled_angle

        if abs(remaining_distance) <= 0.01 and abs(remaining_angle) <= 0.01:
            self.get_logger().info(f'Target reached. Traveled distance: {self.traveled_distance} m, Traveled angle: {self.traveled_angle} radians.')
            self.publish_zero_speeds()
            # Trigger lifecycle state changes to reset the node
            self.trigger_transition(LifecycleState.TRANSITION_DEACTIVATE)
            self.trigger_transition(LifecycleState.TRANSITION_CLEANUP)
            self.trigger_transition(LifecycleState.TRANSITION_CONFIGURE)
            self.trigger_transition(LifecycleState.TRANSITION_ACTIVATE)
            return

        linear_speed, angular_speed = self.calculate_speeds(remaining_distance, remaining_angle, dt)
        wheel_speeds = self.calculate_wheel_speeds(linear_speed, angular_speed)
        self.traveled_distance += linear_speed * dt
        self.traveled_angle += angular_speed * dt
        self.publish_wheel_speeds(wheel_speeds)

    def publish_zero_speeds(self):
        wheel_speed_msg = Float64MultiArray()
        wheel_speed_msg.data = [0.0, 0.0]
        self.wheel_cmd_pub.publish(wheel_speed_msg)

    def calculate_speeds(self, remaining_distance, remaining_angle, dt):
        linear_speed = np.sign(remaining_distance) * min(self.max_speed, abs(remaining_distance) / dt)
        angular_speed = np.sign(remaining_angle) * min(self.max_speed / self.wheel_separation, abs(remaining_angle) / dt)
        if abs(remaining_distance) < 0.2:
            linear_speed *= abs(remaining_distance / 0.2)
        if abs(remaining_angle) < 0.1:
            angular_speed *= abs(remaining_angle / 0.1)
        return linear_speed, angular_speed

    def calculate_wheel_speeds(self, linear_speed, angular_speed):
        speed_conversion = np.array([[self.wheel_radius / 2, self.wheel_radius / 2],
                                     [self.wheel_radius / self.wheel_separation, -self.wheel_radius / self.wheel_separation]])
        return np.matmul(speed_conversion, np.array([linear_speed, angular_speed]))

    def publish_wheel_speeds(self, wheel_speeds):
        wheel_speed_msg = Float64MultiArray()
        wheel_speed_msg.data = wheel_speeds.tolist()
        self.wheel_cmd_pub.publish(wheel_speed_msg)

def main():
    rclpy.init()
    wheel_controller = WheelController()
    rclpy.spin(wheel_controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
