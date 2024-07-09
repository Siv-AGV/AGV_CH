import rclpy
from rclpy.node import Node
from canopen_interfaces.msg import COData
from std_msgs.msg import Float32

class WheelSpeedCompare(Node):
    def __init__(self):
        super().__init__('wheel_speed_compare')
        
        # Subscribers
        self.subscription_motorL_pre = self.create_subscription(
            COData,
            '/motorL/tpdo_pre',
            self.listener_callback_motorL_pre,
            10)
        self.subscription_motorL_pre  # prevent unused variable warning

        self.subscription_motorR_pre = self.create_subscription(
            COData,
            '/motorR/tpdo_pre',
            self.listener_callback_motorR_pre,
            10)
        self.subscription_motorR_pre  # prevent unused variable warning

        self.subscription_motorL_post = self.create_subscription(
            COData,
            '/motorL/tpdo_post',
            self.listener_callback_motorL_post,
            10)
        self.subscription_motorL_post  # prevent unused variable warning

        self.subscription_motorR_post = self.create_subscription(
            COData,
            '/motorR/tpdo_post',
            self.listener_callback_motorR_post,
            10)
        self.subscription_motorR_post  # prevent unused variable warning

        # Publisher
        self.publisher_ = self.create_publisher(Float32, 'troubleshoot_correction', 10)

        # Storage for pre and post data
        self.motorL_pre = None
        self.motorR_pre = None
        self.motorL_post = None
        self.motorR_post = None

    def listener_callback_motorL_pre(self, msg):
        self.motorL_pre = msg
        self.publish_difference()

    def listener_callback_motorR_pre(self, msg):
        self.motorR_pre = msg
        self.publish_difference()

    def listener_callback_motorL_post(self, msg):
        self.motorL_post = msg
        self.publish_difference()

    def listener_callback_motorR_post(self, msg):
        self.motorR_post = msg
        self.publish_difference()

    def publish_difference(self):
        if self.motorL_pre and self.motorR_pre and self.motorL_post and self.motorR_post:
            diff_motorL = self.motorL_post.data - self.motorL_pre.data
            diff_motorR = self.motorR_post.data - self.motorR_pre.data
            self.get_logger().info(f'Difference Motor L: {diff_motorL}, Motor R: {diff_motorR}')
            
            # Example: average the differences to publish
            average_diff = (diff_motorL + diff_motorR) / 2
            msg = Float32()
            msg.data = average_diff
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = WheelSpeedCompare()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
