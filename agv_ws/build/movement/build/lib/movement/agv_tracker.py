#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64
import numpy as np
import matplotlib.pyplot as plt

class AGVTracker(Node):
    def __init__(self):
        super().__init__('agv_tracker')
        self.subscription = self.create_subscription(Float64MultiArray, 'corrected_wheel_speeds', self.wheel_speed_callback, 10)
        self.distance_remaining_pub = self.create_publisher(Float64, 'distance_remaining', 10)
        self.angle_remaining_pub = self.create_publisher(Float64, 'angle_remaining', 10)

        self.wheel_radius = 0.0875
        self.wheel_separation = 0.657

        self.x_position = 0.0
        self.y_position = 0.0
        self.orientation = 0.0  # Orientation angle in radians

        self.initial_distance = 0.0
        self.initial_angle = 0.0
        self.traveled_distance = 0.0

        self.fig, self.ax = plt.subplots()
        self.path_x = []
        self.path_y = []
        self.timer = self.create_timer(0.1, self.update_plot)

    def wheel_speed_callback(self, msg):
        wheel_speed_left = msg.data[0]
        wheel_speed_right = msg.data[1]

        # Calculate linear and angular velocities
        linear_velocity = (wheel_speed_left + wheel_speed_right) * self.wheel_radius / 2.0
        angular_velocity = (wheel_speed_right - wheel_speed_left) * self.wheel_radius / self.wheel_separation

        # Update position and orientation
        dt = 0.1  # Assuming the callback is called every 0.1 seconds
        self.x_position += linear_velocity * np.cos(self.orientation) * dt
        self.y_position += linear_velocity * np.sin(self.orientation) * dt
        self.orientation += angular_velocity * dt

        self.path_x.append(self.x_position)
        self.path_y.append(self.y_position)

        # Calculate remaining distance and angle
        distance_remaining = self.initial_distance - self.traveled_distance
        angle_remaining = self.initial_angle - self.orientation

        # Publish remaining distance and angle
        distance_msg = Float64()
        distance_msg.data = distance_remaining
        self.distance_remaining_pub.publish(distance_msg)

        angle_msg = Float64()
        angle_msg.data = angle_remaining
        self.angle_remaining_pub.publish(angle_msg)

    def update_plot(self):
        self.ax.clear()
        self.ax.plot(self.path_x, self.path_y, label='AGV Path')
        self.ax.set_xlabel('X Position (m)')
        self.ax.set_ylabel('Y Position (m)')
        self.ax.set_title('AGV Position in X-Y Plane')
        self.ax.legend()
        self.ax.grid(True)
        plt.pause(0.1)

    def run(self, initial_distance, initial_angle):
        self.initial_distance = initial_distance
        self.initial_angle = initial_angle
        plt.ion()
        plt.show()

def main(args=None):
    rclpy.init(args=args)
    agv_tracker = AGVTracker()

    # Simulate initial inputs
    initial_distance = 5.0  # Example distance in meters
    initial_angle = np.radians(30)  # Example angle in radians
    agv_tracker.run(initial_distance, initial_angle)

    rclpy.spin(agv_tracker)
    agv_tracker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
