import rclpy
from rclpy.node import Node
from canopen_interfaces.msg import COData
import numpy as np
import math

class CanPublisher(Node):
    def __init__(self):
        super().__init__("can_publisher")

        self.publisher_L = self.create_publisher(COData, '/motorL/tpdo', 10)
        self.publisher_R = self.create_publisher(COData, '/motorR/tpdo', 10)
        
        self.wheel_radius = 0.0875
        self.wheel_separation = 0.657

        self.speed_conversion = np.array([[self.wheel_radius / 2, self.wheel_radius / 2],
                                          [self.wheel_radius / self.wheel_separation, -self.wheel_radius / self.wheel_separation]])

        self.current_wheel_speed_conv_L = 0
        self.current_wheel_speed_conv_R = 0
        self.current_wheel_speed_conv_L_hex = 0
        self.current_wheel_speed_conv_R_hex = 0

        self.create_timer(0.1, self.update_wheel_speeds)

    def decimal_to_hex(self, decimal_value, bit_length=32):
        if decimal_value >= 0:
            return int(decimal_value)
        else:
            two_complement_value = (1 << bit_length) + decimal_value
            return int(two_complement_value)

    def update_wheel_speeds(self):
        agv_speed = np.array([[0.5], [0.1]])  # Example speeds: linear 0.5 m/s, angular 0.1 rad/s
        wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion), agv_speed)

        self.current_wheel_speed_conv_L = int(np.nan_to_num(((wheel_speed[0] / (2 * math.pi)) * 60 * 20 * 512 * 10000) / 1875))
        self.current_wheel_speed_conv_R = -int(np.nan_to_num(((wheel_speed[1] / (2 * math.pi)) * 60 * 20 * 512 * 10000) / 1875))
        self.current_wheel_speed_conv_L_hex = self.decimal_to_hex(self.current_wheel_speed_conv_L)
        self.current_wheel_speed_conv_R_hex = self.decimal_to_hex(self.current_wheel_speed_conv_R)

        self.publish_wheel_speed_L()
        self.publish_wheel_speed_R()

    def publish_wheel_speed_L(self):
        msg0 = COData()
        msg0.index = 0x60FF
        msg0.subindex = 0
        msg0.data = self.current_wheel_speed_conv_L_hex
        self.publisher_L.publish(msg0)

    def publish_wheel_speed_R(self):
        msg1 = COData()
        msg1.index = 0x60FF
        msg1.subindex = 0
        msg1.data = self.current_wheel_speed_conv_R_hex
        self.publisher_R.publish(msg1)

def main(args=None):
    rclpy.init()
    can_publisher = CanPublisher()
    rclpy.spin(can_publisher)
    can_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
