import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class WheelSpeedPublisher(Node):
    def __init__(self):
        super().__init__('wheel_speed_publisher')
        self.publisher_ = self.create_publisher(Float64, 'wheel_speed', 10)
        self.subscription = self.create_subscription(Float64, 'wheel_speed_control', self.callback, 10)

    def callback(self, msg):
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    wheel_speed_publisher = WheelSpeedPublisher()
    rclpy.spin(wheel_speed_publisher)
    wheel_speed_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
