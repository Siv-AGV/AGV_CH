import rclpy
from rclpy.node import Node
from canopen_interfaces.srv import COWrite
from canopen_interfaces.msg import COData

class CODataPublisher(Node):
    def __init__(self):
        super().__init__('co_data_publisher')
        self.service = self.create_service(COWrite, 'cowrite_service', self.handle_cowrite_request)
        self.publisher_ = self.create_publisher(COData, '/motorL/tpdo', 10)
        self.timer = self.create_timer(0.1, self.publish_wheel_speed)
        self.index = 0
        self.subindex = 0
        self.data = 0

    def handle_cowrite_request(self, request, response):
        self.index = request.index
        self.subindex = request.subindex
        self.data = request.data

        self.get_logger().info('Received new data: %d' % self.data)
        print (type(self.data))
        response.success = True
        return response

    def publish_wheel_speed(self):
        msg = COData()
        msg.index = self.index
        msg.subindex = self.subindex
        msg.data = self.data
        self.publisher_.publish(msg)
        self.data_hex = hex(self.data)
        print (self.data_hex)
        

def main(args=None):
    rclpy.init(args=args)
    co_data_publisher = CODataPublisher()
    rclpy.spin(co_data_publisher)
    co_data_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
