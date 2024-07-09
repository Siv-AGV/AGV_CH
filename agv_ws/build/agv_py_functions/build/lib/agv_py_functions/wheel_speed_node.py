import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SetWheelSpeedNode(Node):
    def __init__(self):
        super().__init__('set_wheel_speed_node')

        # Initialize a publisher to publish the wheel speed
        self.wheel_speed_pub = self.create_publisher(Float32, 'set_wheel_speed', 10)

        # Set the initial wheel speed
        self.wheel_speed = 200.0 #set your speed here!!!

        # Create a timer to periodically publish the wheel speed (for demonstration)
        self.timer = self.create_timer(1.0, self.publish_wheel_speed)

    def publish_wheel_speed(self):
        msg = Float32()
        msg.data = self.wheel_speed
        self.wheel_speed_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    set_wheel_speed_node = SetWheelSpeedNode()
    try:
        rclpy.spin(set_wheel_speed_node)
    except KeyboardInterrupt:
        pass

    set_wheel_speed_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
