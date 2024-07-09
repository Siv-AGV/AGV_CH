import rclpy
from rclpy.node import Node
from agv_msgs.srv import SetPGVValues

class SetPGVClient(Node):
    def __init__(self):
        super().__init__('set_pgv_client')
        self.cli = self.create_client(SetPGVValues, 'set_pgv_values')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SetPGVValues.Request()

    def send_request(self, x_offset, y_offset, z_offset):
        self.req.x_offset = x_offset
        self.req.y_offset = y_offset
        self.req.z_offset = z_offset
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    client = SetPGVClient()
    try:
        while rclpy.ok():
            x_offset = float(input("Enter x_offset: "))
            y_offset = float(input("Enter y_offset: "))
            z_offset = float(input("Enter z_offset: "))
            response = client.send_request(x_offset, y_offset, z_offset)
            print(f'Success: {response.success}, Message: {response.message}')
    except KeyboardInterrupt:
        pass
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
