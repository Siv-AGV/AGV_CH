#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import Twist
from action_msgs.msg import GoalStatus
from action_tutorials_interfaces.action import Move
import numpy as np

class WheelController(Node):
    def __init__(self):
        super().__init__('wheel_controller')
        self.action_server = ActionServer(
            self,
            Move,
            'move',
            self.execute_callback
        )
        self.declare_parameter("wheel_radius", 0.0875)
        self.declare_parameter("wheel_separation", 0.657)
        self.declare_parameter("max_acceleration", 0.1)
        self.declare_parameter("max_speed", 0.2)

        self.wheel_radius = self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_separation = self.get_parameter("wheel_separation").get_parameter_value().double_value
        self.max_acceleration = self.get_parameter("max_acceleration").get_parameter_value().double_value
        self.max_speed = self.get_parameter("max_speed").get_parameter_value().double_value

        self.current_wheel_speed = np.array([0.0, 0.0])
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0
        self.timer = None

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing motion...')
        feedback_msg = Move.Feedback()
        result = Move.Result()

        command = goal_handle.request.command
        target_distance = command.linear.x
        target_angle = command.angular.z

        feedback_msg.current_distance = 0.0
        feedback_msg.current_angle = 0.0

        # Simulate movement by updating traveled distance and angle
        while abs(feedback_msg.current_distance) < abs(target_distance) or abs(feedback_msg.current_angle) < abs(target_angle):
            if abs(feedback_msg.current_distance) < abs(target_distance):
                feedback_msg.current_distance += target_distance / 10.0
            if abs(feedback_msg.current_angle) < abs(target_angle):
                feedback_msg.current_angle += target_angle / 10.0
            goal_handle.publish_feedback(feedback_msg)
            rclpy.sleep(0.1)

        result.completed = True
        goal_handle.succeed()
        return result

def main(args=None):
    rclpy.init(args=args)
    wheel_controller = WheelController()
    executor = MultiThreadedExecutor()
    rclpy.spin(wheel_controller, executor=executor)

    wheel_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
