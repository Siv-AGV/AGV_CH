#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher')
        self.publisher_ = self.create_publisher(Twist, 'command_topic', 10)
        self.send_commands()

    def send_commands(self):
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

                msg = Twist()
                if choice == 0:
                    msg.linear.x = 1.0  # Move forward 1 meter
                    msg.angular.z = 0.0  # No rotation
                elif choice == 1:
                    msg.linear.x = -1.0  # Move backward 1 meter
                    msg.angular.z = 0.0  # No rotation
                elif choice == 2:
                    msg.linear.x = 0.0  # No linear movement
                    msg.angular.z = math.pi / 2  # Rotate 90 degrees clockwise
                elif choice == 3:
                    msg.linear.x = 0.0  # No linear movement
                    msg.angular.z = -math.pi / 2  # Rotate 90 degrees counterclockwise
                else:
                    self.get_logger().info('Invalid input, please enter a number between 0 and 4.')
                    continue

                self.publisher_.publish(msg)
                self.get_logger().info('Publishing: Move {:.1f} m, Rotate {:.2f} radians'.format(msg.linear.x, msg.angular.z))

            except ValueError:
                self.get_logger().info('Invalid input, please enter a valid integer.')

def main(args=None):
    rclpy.init(args=args)
    command_publisher = CommandPublisher()
    rclpy.spin(command_publisher)
    command_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
