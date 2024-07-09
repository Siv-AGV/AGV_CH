#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64
from pgv100.msg import PGVScan  # Assuming this message type for QR scanner data
import numpy as np
from canopen_interfaces.msg import COData

class OffsetCorrector(Node):
    def __init__(self):
        super().__init__('offset_corrector')
        self.declare_parameter('wheel_radius', 0.0875)
        self.declare_parameter('wheel_separation', 0.657)
        self.wheel_radius = self.get_parameter('wheel_radius').get_parameter_value().double_value
        self.wheel_separation = self.get_parameter('wheel_separation').get_parameter_value().double_value

        self.subscription = self.create_subscription(PGVScan, 'PGV_Scan', self.offset_callback, 10)
        self.corrected_wheel_speed_pub = self.create_publisher(Float64MultiArray, 'corrected_wheel_speeds', 10)
        self.travel_distance_sub = self.create_subscription(Float64, 'traveled_dist', self.distance_callback, 10)
        self.remaining_distance_sub = self.create_subscription(Float64, 'remaining_dist', self.remaining_distance_callback, 10)
        self.original_wheel_speed_sub = self.create_subscription(Float64MultiArray, 'wheel_speeds', self.original_wheel_speed_callback, 10)

        # self.publisher_L = self.create_publisher(COData, '/motorL/tpdo_post', 10) #change to wheel topic
        # self.publisher_R = self.create_publisher(COData, '/motorR/tpdo_post', 10) #change to wheel topic

        
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.offset_z = 0.0
        self.traveled_distance = 0.0
        self.remaining_distance = 0.0
        self.last_correction_distance = 0.0

        self.original_wheel_speeds = np.array([0.0, 0.0])

        self.speed_conversion = np.array([[self.wheel_radius / 2, self.wheel_radius / 2],
                                          [self.wheel_radius / self.wheel_separation, -self.wheel_radius / self.wheel_separation]])

    def offset_callback(self, msg):
        self.offset_x = msg.x_position
        self.offset_y = msg.x_position
        self.offset_z = msg.angle

    def distance_callback(self, msg):
        self.traveled_distance = msg.data

        # Check if more than 1.5m left to travel
        if self.remaining_distance > 1.5 and self.traveled_distance - self.last_correction_distance >= 1.5:
            self.correct_for_offset()
            self.last_correction_distance = self.traveled_distance

    def remaining_distance_callback(self, msg):
        self.remaining_distance = msg.data

    def original_wheel_speed_callback(self, msg):
        self.original_wheel_speeds = np.array([msg.data[0], msg.data[1]])

    def correct_for_offset(self):
        linear_correction = self.calculate_linear_correction(self.offset_x, self.offset_y)
        angular_correction = self.calculate_angular_correction(self.offset_z)

        # Combine the linear and angular corrections
        agv_correction = np.array([[linear_correction], [angular_correction]])
        wheel_speed_correction = np.matmul(np.linalg.inv(self.speed_conversion), agv_correction)

        # Add the correction to the original wheel speeds
        corrected_wheel_speeds = self.original_wheel_speeds + wheel_speed_correction.flatten()

        corrected_wheel_speed_msg = Float64MultiArray()
        corrected_wheel_speed_msg.data = [corrected_wheel_speeds[0], corrected_wheel_speeds[1]]
        self.corrected_wheel_speed_pub.publish(corrected_wheel_speed_msg)

        

        
        # self.publisher_L.publish(corrected_wheel_speed_msg[0])
        # self.publisher_R.publish(corrected_wheel_speed_msg[1])

        
        self.get_logger().info(f"Published corrected wheel speeds: {corrected_wheel_speeds[0]}, {corrected_wheel_speeds[1]}")

    def calculate_linear_correction(self, offset_x, offset_y):
        # Apply the linear offset correction formula
        return np.sqrt(offset_x**2 + offset_y**2)

    def calculate_angular_correction(self, offset_z):
        # Apply the angular offset correction formula
        return offset_z
    
       
    
    # def publish_wheel_speed_L_corrected(self):
    #     msg0 = COData()
    #     msg0.index = 0x60FF
    #     msg0.subindex = 0
    #     msg0.data = self.current_wheel_speed_conv_L_hex
    #     self.publisher_L.publish(msg0)

    # def publish_wheel_speed_R_corrected(self):
    #     msg0 = COData()
    #     msg0.index = 0x60FF
    #     msg0.subindex = 0
    #     msg0.data = self.current_wheel_speed_conv_L_hex
    #     self.publisher_L.publish(msg0)

def main(args=None):
    rclpy.init(args=args)
    offset_corrector = OffsetCorrector()
    rclpy.spin(offset_corrector)
    offset_corrector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
