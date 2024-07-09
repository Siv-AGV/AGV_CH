#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import Twist
from action_tutorials_interfaces.action import Move
import math

class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher')
        self.action_client = ActionClient(self, Move, 'move')
        self.send_commands()

    def send_commands(self):
        self.action_client.wait_for_server()

        while True:
            print("Enter a command number:")
            print("0 - Move forward 1 meter")
            print("1 - Move backward 1 meter")
            print("2 - Rotate 90 degrees clockwise")
            print("3 - Rotate 90 degrees counterclockwise")
            print("4 - Exit")
            user_input = input("Please enter your choice: ")

            try:
                choice = int(user_input)
                if choice == 4:
                    self.get_logger().info('Exiting publisher.')
                    break

                goal_msg = Move.Goal()
                if choice == 0:
                    goal_msg.command.linear.x = 1.0
                elif choice == 1:
                    goal_msg.command.linear.x = -1.0
                elif choice == 2:
                    goal_msg.command.angular.z = math.pi / 2
                elif choice == 3:
                    goal_msg.command.angular.z = -math.pi / 2
                else:
                    continue

                self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
                self.get_logger().info('Command sent.')
            except ValueError:
                self.get_logger().info('Please enter a valid number.')

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'Moving... Current distance: {feedback_msg.feedback.current_distance} m, Current angle: {feedback_msg.feedback.current_angle} radians')

def main(args=None):
    rclpy.init(args=args)
    command_publisher = CommandPublisher()
    rclpy.spin(command_publisher)
    command_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
