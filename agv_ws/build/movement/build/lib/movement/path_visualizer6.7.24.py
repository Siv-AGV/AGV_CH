#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray, Float64
from geometry_msgs.msg import PoseArray, Pose
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation
import threading

class PathVisualizer(Node):
    def __init__(self):
        super().__init__("path_visualizer")
        self.pose_array_pub = self.create_publisher(PoseArray, 'path', 10)
        self.wheel_speed_sub = self.create_subscription(Float64MultiArray, 'wheel_speeds', self.wheel_speed_callback, 10)
        self.traveled_distance_sub = self.create_subscription(Float64, 'traveled_dist', self.traveled_distance_callback, 10)
        self.remaining_distance_sub = self.create_subscription(Float64, 'remaining_dist', self.remaining_distance_callback, 10)

        self.pose_array = PoseArray()
        self.current_pose = Pose()
        self.current_pose.position.x = 0.0
        self.current_pose.position.y = 0.0
        self.current_pose.position.z = 0.0
        self.current_pose.orientation.w = 1.0

        self.fig, self.ax = plt.subplots()
        self.x_data = []
        self.y_data = []

        self.init_plot()

        self.ax_clear_button = plt.axes([0.8, 0.01, 0.1, 0.05])
        self.clear_button = Button(self.ax_clear_button, 'Clear')
        self.clear_button.on_clicked(self.clear_plot)

        self.text_x = self.ax.text(1.05, 0.5, '', transform=self.ax.transAxes)
        self.text_y = self.ax.text(1.05, 0.45, '', transform=self.ax.transAxes)
        self.text_theta = self.ax.text(1.05, 0.4, '', transform=self.ax.transAxes)

        self.ani = FuncAnimation(self.fig, self.update_plot, interval=100)

    def init_plot(self):
        station_distance = 1.5
        num_stations_x = 6
        num_stations_y = 5
        for i in range(num_stations_x):
            for j in range(num_stations_y):
                x = i * station_distance
                y = j * station_distance
                self.ax.plot(x, y, marker='x', color='red')
        self.ax.set_xlim(-1, num_stations_x * station_distance + 1)
        self.ax.set_ylim(-1, num_stations_y * station_distance + 1)
        self.ax.set_aspect('equal')

    def wheel_speed_callback(self, msg):
        left_wheel_speed = msg.data[0]
        right_wheel_speed = msg.data[1]
        self.update_position(left_wheel_speed, right_wheel_speed)

    def traveled_distance_callback(self, msg):
        traveled_distance = msg.data

    def remaining_distance_callback(self, msg):
        remaining_distance = msg.data

    def update_position(self, left_wheel_speed, right_wheel_speed):
        wheel_radius = 0.0875  # same as in SimpleController
        wheel_separation = 0.657  # same as in SimpleController

        v = (left_wheel_speed + right_wheel_speed) * wheel_radius / 2.0
        omega = (right_wheel_speed - left_wheel_speed) * wheel_radius / wheel_separation

        dt = 0.1  # Assume update interval same as SimpleController timer
        delta_x = v * np.cos(self.current_pose.orientation.z) * dt
        delta_y = v * np.sin(self.current_pose.orientation.z) * dt
        delta_theta = omega * dt

        self.current_pose.position.x += delta_x
        self.current_pose.position.y += delta_y
        self.current_pose.orientation.z += delta_theta

        self.pose_array.poses.append(self.current_pose)

        self.x_data.append(self.current_pose.position.x)
        self.y_data.append(self.current_pose.position.y)

    def update_plot(self, frame):
        self.ax.clear()
        self.init_plot()
        self.ax.plot(self.x_data, self.y_data, marker='o')

        # Draw pointer for orientation
        if len(self.x_data) > 0:
            last_x = self.x_data[-1]
            last_y = self.y_data[-1]
            theta = self.current_pose.orientation.z
            pointer_length = 0.5
            pointer_x = last_x + pointer_length * np.cos(theta)
            pointer_y = last_y + pointer_length * np.sin(theta)
            self.ax.plot([last_x, pointer_x], [last_y, pointer_y], color='blue', marker='o')

        # Update live text
        self.text_x.set_text(f'X: {self.current_pose.position.x:.2f}')
        self.text_y.set_text(f'Y: {self.current_pose.position.y:.2f}')
        self.text_theta.set_text(f'θ: {np.degrees(self.current_pose.orientation.z):.2f}°')

        self.ax.set_xlabel('X position (m)')
        self.ax.set_ylabel('Y position (m)')
        self.ax.set_title('Top Down Path Visualization')
        self.fig.canvas.draw()

    def clear_plot(self, event):
        self.x_data.clear()
        self.y_data.clear()
        self.current_pose.position.x = 0.0
        self.current_pose.position.y = 0.0
        self.current_pose.orientation.z = 0.0
        self.update_plot(None)

def ros_spin(node):
    rclpy.spin(node)

def main(args=None):
    rclpy.init(args=args)
    visualizer = PathVisualizer()

    ros_thread = threading.Thread(target=ros_spin, args=(visualizer,))
    ros_thread.start()

    plt.show()

    visualizer.destroy_node()
    rclpy.shutdown()
    ros_thread.join()

if __name__ == '__main__':
    main()
