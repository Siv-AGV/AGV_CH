import rclpy
from rclpy.node import Node
from agv_msgs.srv import SetWheelSpeed
from std_msgs.msg import Float64

class WheelSpeedServer(Node):
    def __init__(self):
        super().__init__('wheel_speed_server')
        self.declare_parameter('wheel_speed', 0.0)
        self.wheel_speed = self.get_parameter('wheel_speed').value
        self.server = self.create_service(SetWheelSpeed, 'set_wheel_speed', self.set_wheel_speed_callback)
        self.publisher_ = self.create_publisher(Float64, 'wheel_speed_control', 10)
        self.timer = self.create_timer(0.1, self.publish_wheel_speed)

    def set_wheel_speed_callback(self, request, response):
        self.wheel_speed = request.data
        self.get_logger().info('Received new wheel speed: %f' % self.wheel_speed)
        self.publish_wheel_speed()
        response.message = "speed updated successfully"
        return response

    def publish_wheel_speed(self):
        msg = Float64()
        msg.data = self.wheel_speed
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    wheel_speed_server = WheelSpeedServer()
    rclpy.spin(wheel_speed_server)
    wheel_speed_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
