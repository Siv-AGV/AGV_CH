import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetWheelSpeed

def set_wheel_speed_client():
    rclpy.init()
    node = rclpy.create_node('set_wheel_speed_client')
    client = node.create_client(SetWheelSpeed, 'set_wheel_speed_service')

    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('Service not available, waiting again...')
    request = SetWheelSpeed.Request()
    request.data = True  # Set the request to True to indicate setting the wheel speed

    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        response = future.result()
        node.get_logger().info('Service call succeeded: %s' % response.message)
    else:
        node.get_logger().info('Service call failed')

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    set_wheel_speed_client()
