import rclpy
from rclpy.node import Node
from canopen_interfaces.msg import COData


class SpeedServiceClient(Node):
    def __init__(self):
        super().__init__('speed_service_client')
        self.client = self.create_client(COData, 'wheel_speed_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

    def send_request(self, index, subindex, data):
        request = COData.Request()
        request.index = index
        request.subindex = subindex
        request.data = data
        future = self.client.call_async(request)
        future.add_done_callback(self.callback)

    def callback(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info('Wheel speed set successfully')
            else:
                self.get_logger().info('Failed to set wheel speed')
        except Exception as e:
            self.get_logger().info('Service call failed: %r' % (e,))

def main(args=None):
    rclpy.init(args=args)
    speed_service_client = SpeedServiceClient()
    while rclpy.ok():
        try:
            index_input = input("Enter index (default: 0x60FF): ")
            index = int(index_input, 16) if index_input else 0x60FF
            subindex_input = input("Enter subindex (default: 0): ")
            subindex = int(subindex_input) if subindex_input else 0
            data = int(input("Enter data (uint32): "))
            speed_service_client.send_request(index, subindex, data)
        except ValueError:
            print("Please enter valid integer values")
    speed_service_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
