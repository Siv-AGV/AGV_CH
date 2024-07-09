#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from agv_msgs.srv import Move
import math

class CommandClient(Node):
    def __init__(self):
        super().__init__('command_client')
        self.client = self.create_client(Move, 'wheel_control_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.get_command()

    def get_command(self):
        print("Enter a command:")
        print("0 - Move forward")
        print("1 - Move backward")
        print("2 - Rotate 90 degrees clockwise")
        print("3 - Rotate 90 degrees counterclockwise")
        print("4 - Rotate 180 degrees clockwise")
        print("5 - Rotate 180 degrees counterclockwise")
        print("6 - Exit")
        user_input = input("Please enter your choice: ")

        try:
            choice = int(user_input)
            if choice == 6:
                self.get_logger().info('Exiting publisher.')
                rclpy.shutdown()
                return

            msg = Twist()
            if choice in [0, 1]:
                distance_x = float(input("Please enter the distance in the x direction (in meters): "))
                distance_y = float(input("Please enter the distance in the y direction (in meters): "))
                angle_z = float(input("Please enter the rotation angle around z-axis (in degrees): "))
                msg.linear.x = distance_x if choice == 0 else -distance_x
                msg.linear.y = distance_y if choice == 0 else -distance_y
                msg.angular.z = math.radians(angle_z) if choice == 0 else -math.radians(angle_z)
            elif choice in [2, 3, 4, 5]:
                angle = 90 if choice in [2, 3] else 180
                msg.angular.z = math.radians(angle) if choice in [2, 4] else -math.radians(angle)

            request = Move.Request()
            request.command = msg
            future = self.client.call_async(request)
            future.add_done_callback(self.future_callback)

        except ValueError:
            self.get_logger().info('Invalid input, please enter a valid integer for choice and valid numbers for distances and angle.')
            self.get_command()  # Prompt again on invalid input

    def future_callback(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info('Command completed successfully')
                self.get_command()  # Prompt for the next command after successful completion
            else:
                self.get_logger().info('Command execution failed')
                self.get_command()  # Optionally prompt again if execution failed
        except Exception as e:
            self.get_logger().info('Service call failed: %r' % e)
            self.get_command()  # Optionally prompt again if call failed

def main(args=None):
    rclpy.init(args=args)
    client = CommandClient()
    rclpy.spin(client)
    # Clean up is done within the CommandClient class

if __name__ == '__main__':
    main()
