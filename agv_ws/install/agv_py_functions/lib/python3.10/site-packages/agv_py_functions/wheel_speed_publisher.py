import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class WheelSpeedPublisher(Node):
    def __init__(self):
        super().__init__('wheel_speed_publisher')

        # Initialize a publisher to publish the wheel speed
        self.wheel_speed_pub = self.create_publisher(Float32, 'wheel_speed', 10)

        # Set the initial wheel speed to 0
        self.wheel_speed = 0.0

        # Subscribe to Node 1 to receive the wheel speed
        self.create_subscription(Float32, 'set_wheel_speed', self.wheel_speed_callback, 10)

        # Create a timer to periodically publish the wheel speed
        self.timer = self.create_timer(0.01, self.publish_wheel_speed)

    def wheel_speed_callback(self, msg):
        # Update the wheel speed when a new message is received from Node 1
        self.wheel_speed = msg.data

    def publish_wheel_speed(self):
        msg = Float32()
        msg.data = self.wheel_speed
        self.wheel_speed_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    wheel_speed_publisher = WheelSpeedPublisher()
    try:
        rclpy.spin(wheel_speed_publisher)
    except KeyboardInterrupt:
        pass

    wheel_speed_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
