import rclpy
from rclpy.node import Node
from pgv100.msg import PGVScan
from agv_msgs.srv import SetPGVValues

class MockPGVPublisher(Node):
    def __init__(self):
        super().__init__('mock_pgv')
        self.publisher_ = self.create_publisher(PGVScan, 'pgv_scan', 10)
        self.service = self.create_service(SetPGVValues, 'set_pgv_values', self.set_pgv_values_callback)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.publish_message)

        # Initialize the offsets
        self.x_offset = 0.0
        self.y_offset = 0.0
        self.z_offset = 0.0

    def set_pgv_values_callback(self, request, response):
        self.x_offset = request.x_offset
        self.y_offset = request.y_offset
        self.z_offset = request.z_offset

        response.success = True
        response.message = "Offsets set successfully"
        self.get_logger().info(f'Set new offsets: x_offset={self.x_offset}, y_offset={self.y_offset}, z_offset={self.z_offset}')
        return response

    def publish_message(self):
        msg = PGVScan()
        msg.x_position = self.x_offset
        msg.y_position = self.y_offset
        msg.angle = self.z_offset
        msg.direction = 'right'
        msg.color_lane_count = 0
        msg.no_color_lane = 1
        msg.no_position = 2
        msg.tag_detected = 3

        self.publisher_.publish(msg)
        # self.get_logger().info(f'Publishing: {msg}')

def main(args=None):
    rclpy.init(args=args)
    mock_pgv_publisher = MockPGVPublisher()
    rclpy.spin(mock_pgv_publisher)
    mock_pgv_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
