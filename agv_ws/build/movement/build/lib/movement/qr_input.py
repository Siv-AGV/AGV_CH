#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from pgv100.msg import PGVScan
from std_msgs.msg import Float64MultiArray
import math

class QRInput(Node):
    def __init__(self):
        super().__init__('qr_input')
        self.publisher_ = self.create_publisher(Float64MultiArray, 'pgv_converted', 10)
        self.pgv_subscriber = self.create_subscription(PGVScan, 'pgv_scan', self.pgv_callback, 10)
        self.get_logger().info("QR Input node initialized.")

    def convert_pgv_values(self, pgv_msg):
        # Convert values from mm to meters
        x_position_m = pgv_msg.x_position / 1000.0
        y_position_m = pgv_msg.y_position / 1000.0
        self.pgv_tag_detected = pgv_msg.tag_detected

        # Adjust the angle PGV vs AGV orientation
        if pgv_msg.angle >= 0:
            converted_angle = (pgv_msg.angle + 180) % 360
        else:
            converted_angle = (pgv_msg.angle + 180)
        angle_rad = math.radians(converted_angle)

        # Correct the x and y positions based on the AGV orientation
        x_position_adjusted = -x_position_m
        y_position_adjusted = -y_position_m

        # Return the adjusted values
        return x_position_adjusted, y_position_adjusted, angle_rad

    def pgv_callback(self, msg):
        converted_values = self.convert_pgv_values(msg)
        converted_msg = Float64MultiArray()
        converted_msg.data = list(converted_values)
        self.publisher_.publish(converted_msg)
        self.get_logger().info(f"Published converted PGV values: {converted_values}")

def main(args=None):
    rclpy.init(args=args)
    node = QRInput()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
