#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from canopen_interfaces.msg import COData
import numpy as np
import math


class TrayController(Node):
    def __init__(self):
        super().__init__('tray_controller')
        self.subscription = self.create_subscription(
            Float64,
            'agv_angular_speed',
            self.angular_speed_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.publisher = self.create_publisher(COData, '/motorSpin/tpdo', 10)
        self.get_logger().info('Tray Controller Node has been started.')

        # self.timer = self.create_timer(1.0/60.0, self.timer_call_back)
        self.timer = None
        self.last_angular_speed = 0.0
        self.total_angle = 0

        # tuning parameter
        self.spin_sync_tune = 82 #82 makes it drift opposite direction, 80 drift current direction

    def angular_speed_callback(self, msg):
        
        self.angular_speed = msg.data
        print ("angular speed: " + str(self.angular_speed))
          # Invert the angular speed for the tray
        if self.angular_speed!=0.00:
            if self.timer is None:
                self.timer = self.create_timer(1.0/60.0, self.timer_callback)
                self.total_angle = self.total_angle+self.angular_speed*(1/60)
        # elif self.angular_speed == 0.0:
            
        else:
            print ("total_angle = " + str(self.total_angle))
            self.stop_spin()
            if self.timer is not None:
                self.timer.cancel()
                self.timer = None
            
        # tray_motor_speed_hex = self.decimal_to_hex(int(tray_speed * 1000))  # Scale and convert to hex
    

    def stop_spin(self):
        tray_speed_msg = COData()
        tray_speed_msg.index = 0x60FF
        tray_speed_msg.subindex = 0
        tray_speed_msg.data = 0
        self.publisher.publish(tray_speed_msg)
        self.get_logger().info(f'Tray motor stopped')
        self.total_angle = 0 


    def timer_callback(self):
        # angular_speed  = angular_speed
        tray_speed = self.angular_speed
        tray_motor_speed_hex = int(np.nan_to_num(((tray_speed / (2 * math.pi)) * 60 * self.spin_sync_tune * 512 * 10000) / 1875))
        spin_motor_speed_hex = self.decimal_to_hex(tray_motor_speed_hex)
        self.publish_tray_speed(spin_motor_speed_hex)

    def publish_tray_speed(self, speed_hex):
        tray_speed_msg = COData()
        tray_speed_msg.index = 0x60FF
        tray_speed_msg.subindex = 0
        tray_speed_msg.data = speed_hex
        self.publisher.publish(tray_speed_msg)
        self.get_logger().info(f'Tray motor speed published: {speed_hex}')

    def decimal_to_hex(self, decimal_value, bit_length=32):
        if decimal_value >= 0:
            return int(decimal_value)
        else:
            two_complement_value = (1 << bit_length) + decimal_value
            return int(two_complement_value)

def main(args=None):
    rclpy.init(args=args)
    tray_controller = TrayController()
    rclpy.spin(tray_controller)
    tray_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
