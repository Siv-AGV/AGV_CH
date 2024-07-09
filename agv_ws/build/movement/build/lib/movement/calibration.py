#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray, Float64
from geometry_msgs.msg import Twist
from agv_msgs.srv import Move
import numpy as np
import math
from canopen_interfaces.msg import COData
from pgv100.msg import PGVScan

class CalibrationNode(Node):
    def __init__(self):
        super().__init__("calibration_node")
        self.declare_parameter("wheel_radius", 0.0875)
        self.declare_parameter("wheel_separation", 0.657)
        self.declare_parameter("max_acceleration", 0.2)
        self.declare_parameter("max_speed", 1.5)
        self.declare_parameter("tolerance", 0.02)

        self.wheel_radius = self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_separation = self.get_parameter("wheel_separation").get_parameter_value().double_value
        self.max_acceleration = self.get_parameter("max_acceleration").get_parameter_value().double_value
        self.max_speed = self.get_parameter("max_speed").get_parameter_value().double_value
        self.tolerance = self.get_parameter("tolerance").get_parameter_value().double_value

        self.publisher_L = self.create_publisher(COData, '/motorL/tpdo', 10)
        self.publisher_R = self.create_publisher(COData, '/motorR/tpdo', 10)
        self.wheel_speed_pub = self.create_publisher(Float64MultiArray, 'wheel_speeds', 60)
        self.traveled_distance_pub = self.create_publisher(Float64, 'traveled_dist', 60)
        self.remaining_distance_pub = self.create_publisher(Float64, 'remaining_dist', 60)

        self.current_wheel_speed = np.array([0.0, 0.0])
        self.target_distance = 0.0
        self.target_angle = 0.0
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0
        self.traveled_distance_local = 0.0
        self.traveled_distance_old = 0.0
        self.traveled_angle_local = 0.0
        self.traveled_angle_old = 0.0

        self.last_time = None
        self.moving = False

        self.speed_conversion = np.array([[self.wheel_radius / 2, self.wheel_radius / 2],
                                          [self.wheel_radius / self.wheel_separation, -self.wheel_radius / self.wheel_separation]])

        self.pgv_subscriber = self.create_subscription(PGVScan, 'pgv_scan', self.pgv_callback, 10)
        self.correction_data = None

        self.calibration_data = []

    def move_forward(self, distance):
        self.target_distance = distance
        self.target_angle = 0.0
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0
        self.last_time = self.get_clock().now()
        self.moving = True
        self.update_movement()

    def rotate(self, angle):
        self.target_distance = 0.0
        self.target_angle = math.radians(angle)
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0
        self.last_time = self.get_clock().now()
        self.moving = True
        self.update_movement()

    def pgv_callback(self, msg):
        self.latest_qr_data = self.convert_pgv_values(msg)

    def convert_pgv_values(self, pgv_msg):
        x_position_m = pgv_msg.x_position / 1000.0
        y_position_m = pgv_msg.y_position / 1000.0
        converted_angle = (pgv_msg.angle + 180) % 360 if pgv_msg.angle >= 0 else (pgv_msg.angle + 180)
        angle_rad = math.radians(converted_angle)
        x_position_adjusted = x_position_m
        y_position_adjusted = -y_position_m
        return {"x": x_position_adjusted, "y": y_position_adjusted, "orientation": angle_rad}

    def apply_corrections(self):
        if self.correction_data:
            x_position, y_position, angle = self.correction_data["x"], self.correction_data["y"], self.correction_data["orientation"]
            distance_correction = np.sqrt(x_position**2 + y_position**2)
            angle_correction = math.atan2(y_position, 1.0) + angle
            self.target_distance += -distance_correction
            self.target_angle += -angle_correction
            self.get_logger().info(f"Corrections applied: Distance correction: {distance_correction}, Angle correction: {angle_correction}")
            self.correction_data = None

    def perform_calibration_sequence(self):
        initial_position = self.read_qr_code()
        self.move_forward(1.0)
        position_after_forward = self.read_qr_code()
        forward_deviation = self.calculate_deviation(initial_position, position_after_forward)
        print ("forward_deviation: " + str(forward_deviation))

        self.rotate(90)
        position_after_rotation = self.read_qr_code()
        rotation_deviation = self.calculate_deviation(initial_position, position_after_rotation)
        print ("rotation_deviation: " + str(rotation_deviation))

        self.move_forward(1.0)
        self.rotate(180)
        self.move_backward(1.0)
        self.rotate(-180)
        position_after_combination = self.read_qr_code()
        combination_deviation = self.calculate_deviation(initial_position, position_after_combination)
        print ("combination_deviation: " + str(combination_deviation))

        total_deviation = self.combine_errors([forward_deviation, rotation_deviation, combination_deviation])
        self.apply_combined_corrections(total_deviation)


        self.verify_corrections()

    def read_qr_code(self):
        return self.latest_qr_data
               

    def calculate_deviation(self, initial, final):
        delta_x = final.x - initial.x
        delta_y = final.y - initial.y
        delta_orientation = final.orientation - initial.orientation
        return delta_x, delta_y, delta_orientation

    def combine_errors(self, deviations):
        total_x = sum(d[0] for d in deviations)
        total_y = sum(d[1] for d in deviations)
        total_orientation = sum(d[2] for d in deviations)
        return total_x, total_y, total_orientation

    def apply_combined_corrections(self, total_deviation):
        correction_x, correction_y, correction_orientation = total_deviation
        self.calibration_data.append({
            "correction_x": correction_x,
            "correction_y": correction_y,
            "correction_orientation": correction_orientation
        })

    def verify_corrections(self):
        initial_position = self.read_qr_code()
        self.move_forward(1.0)
        position_after_forward = self.read_qr_code()
        forward_deviation = self.calculate_deviation(initial_position, position_after_forward)

        self.rotate(90)
        position_after_rotation = self.read_qr_code()
        rotation_deviation = self.calculate_deviation(initial_position, position_after_rotation)

        self.move_forward(1.0)
        self.rotate(180)
        self.move_backward(1.0)
        self.rotate(-180)
        position_after_combination = self.read_qr_code()
        combination_deviation = self.calculate_deviation(initial_position, position_after_combination)

        total_deviation = self.combine_errors([forward_deviation, rotation_deviation, combination_deviation])

        if abs(total_deviation[0]) <= self.tolerance and abs(total_deviation[1]) <= self.tolerance:
            self.get_logger().info(f"Calibration successful within tolerance: {self.tolerance}")
            self.get_logger().info(f"Final corrections: {self.calibration_data[-1]}")
        else:
            self.get_logger().info(f"Calibration out of tolerance: {self.tolerance}")
            self.get_logger().info(f"Verification result: {total_deviation}")

    def update_movement(self):
        if self.moving:
            current_time = self.get_clock().now()
            dt = (current_time - self.last_time).nanoseconds / 1e9
            self.last_time = current_time

            remaining_distance = self.target_distance - self.traveled_distance
            remaining_angle = self.target_angle - self.traveled_angle

            if abs(remaining_angle) > 0.001:
                angular_speed = self.trapezoidal_velocity_profile(abs(self.target_angle), self.max_speed / self.wheel_separation, self.max_acceleration, abs(self.traveled_angle)) * np.sign(self.target_angle)
            else:
                angular_speed = 0.0
            
            if abs(remaining_distance) > 0.001:
                linear_speed = self.trapezoidal_velocity_profile(abs(self.target_distance), self.max_speed, self.max_acceleration, abs(self.traveled_distance)) * np.sign(self.target_distance)
            else:
                linear_speed = 0.0

            if abs(linear_speed) < 0.001 and remaining_distance != 0:
                linear_speed = np.sign(remaining_distance) * 0.001
            if abs(angular_speed) < 0.001 and remaining_angle != 0:
                angular_speed = np.sign(remaining_angle) * 0.001

            self.traveled_distance += linear_speed * dt
            self.traveled_angle += angular_speed * dt

            self.traveled_distance_local = self.traveled_distance - self.traveled_distance_old

            if self.correction_data:
                if abs(self.traveled_distance_local) >= 1.5:
                    self.apply_corrections()
                    self.traveled_distance_local = 0.0
                    self.traveled_distance_old = self.traveled_distance

            agv_speed = np.array([[linear_speed], [angular_speed]])
            self.wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion), agv_speed)

            self.current_wheel_speed_conv_L = int(np.nan_to_num(((self.wheel_speed[0] / (2 * math.pi)) * 60 * 20 * 512 * 10000) / 1875))
            self.current_wheel_speed_conv_R = -int(np.nan_to_num(((self.wheel_speed[1] / (2 * math.pi)) * 60 * 20 * 512 * 10000) / 1875))
            self.current_wheel_speed_conv_L_hex = self.decimal_to_hex(self.current_wheel_speed_conv_L)
            self.current_wheel_speed_conv_R_hex = self.decimal_to_hex(self.current_wheel_speed_conv_R)

            self.publish_wheel_speeds()
            self.publish_wheel_speed_L()
            self.publish_wheel_speed_R()

            remaining_distance_msg = Float64()
            remaining_distance_msg.data = remaining_distance
            self.remaining_distance_pub.publish(remaining_distance_msg)

            self.get_logger().info(f"Linear speed: {linear_speed}, Angular speed: {angular_speed}, DT: {self.traveled_distance}, RD: {remaining_distance}")

            if abs(remaining_distance) < 0.001 and abs(remaining_angle) < 0.001:
                self.current_wheel_speed = np.array([0.0, 0.0])
                self.moving = False
                self.current_wheel_speed_conv_L = 0
                self.current_wheel_speed_conv_R = 0
                self.current_wheel_speed_conv_L_hex = 0
                self.current_wheel_speed_conv_R_hex = 0
                self.publish_wheel_speed_L()
                self.publish_wheel_speed_R()
                self.get_logger().info("Movement stopped. Target reached.")
                self.traveled_distance_old = 0.0

    def decimal_to_hex(self, decimal_value, bit_length=32):
        if decimal_value >= 0:
            return int(decimal_value)
        else:
            two_complement_value = (1 << bit_length) + decimal_value
            return int(two_complement_value)

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

    def publish_wheel_speeds(self):
        wheel_speed_msg = Float64MultiArray()
        wheel_speed_msg.data = [self.wheel_speed[0, 0], self.wheel_speed[1, 0]]
        self.wheel_speed_pub.publish(wheel_speed_msg)
        traveled_distance_msg = Float64()
        traveled_distance_msg.data = self.traveled_distance
        self.traveled_distance_pub.publish(traveled_distance_msg)

def main(args=None):
    rclpy.init()
    calibration_node = CalibrationNode()
    calibration_node.perform_calibration_sequence()
    calibration_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
