#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
# import can

class CanbusVelocityPublisher(Node):
    def __init__(self):
        super().__init__('canbus_velocity_publisher')
        self.subscription = self.create_subscription(Float64MultiArray, 'velocity_input', self.velocity_callback, 10)
        self.publisher = self.create_publisher(Float64MultiArray, 'canbus_input', 10)
        # self.can_bus = can.interface.Bus()
        self.last_published_velocity = [0, 0]  # Initial value

    def velocity_callback(self, msg):
        wheel_velocities = msg.data
        if wheel_velocities != self.last_published_velocity:
            # Publish wheel velocities to CAN bus topic
            # can_message = can.Message(arbitration_id=0x100, data=[int(velocity) for velocity in wheel_velocities])
            # self.can_bus.send(can_message)
            self.last_published_velocity = wheel_velocities
            self.get_logger().info(f"Published wheel velocities to CAN bus: {wheel_velocities}")
        else:  
            self.last_published_velocity = wheel_velocities

def main(args=None):
    rclpy.init(args=args)
    node = CanbusVelocityPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
