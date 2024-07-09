#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class VelocityInputNode(Node):
    def __init__(self):
        super().__init__('velocity_input_node')
        self.publisher = self.create_publisher(Float64MultiArray, 'velocity_input', 10)
        # self.timer_period = 1.0  # seconds
        # self.timer = self.create_timer(self.timer_period, self.publish_velocity)

    def get_wheel_velocities(self):
        wheel1_velocity = float(input("Enter velocity for wheel 1: "))
        wheel2_velocity = float(input("Enter velocity for wheel 2: "))
        return [wheel1_velocity, wheel2_velocity]

    def publish_velocity(self):
        msg = Float64MultiArray()
        msg.data = self.get_wheel_velocities()
        self.publisher.publish(msg)
        self.get_logger().info(f"Published wheel velocities: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = VelocityInputNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
