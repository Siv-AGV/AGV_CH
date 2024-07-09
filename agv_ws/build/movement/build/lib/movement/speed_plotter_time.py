#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import threading

class SpeedPlotter(Node):
    def __init__(self):
        super().__init__('speed_plotter_time')
        self.subscription = self.create_subscription(
            Float64MultiArray,
            'wheel_speeds',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.fig, self.ax = plt.subplots()
        self.ln1, = self.ax.plot([], [], 'r-', label='Left Wheel Speed')
        self.ln2, = self.ax.plot([], [], 'b-', label='Right Wheel Speed')
        self.xdata, self.ydata1, self.ydata2 = [], [], []
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(-20, 20)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Wheel Speed')
        self.ax.legend()
        self.anim = None

    def listener_callback(self, msg):
        print(f"Received wheel speeds: {msg.data}")
        self.ydata1.append(msg.data[0])
        self.ydata2.append(msg.data[1])
        self.xdata.append(len(self.xdata))

    def update_plot(self, frame):
        self.ln1.set_data(self.xdata, self.ydata1)
        self.ln2.set_data(self.xdata, self.ydata2)
        self.ax.set_xlim(0, max(100, len(self.xdata)))
        return self.ln1, self.ln2,

    def run_animation(self):
        self.anim = FuncAnimation(self.fig, self.update_plot, blit=True)
        plt.show()

def ros_spin(node):
    rclpy.spin(node)

def main(args=None):
    rclpy.init()
    speed_plotter = SpeedPlotter()
    # Start ROS spinning in a separate thread
    spin_thread = threading.Thread(target=ros_spin, args=(speed_plotter,))
    spin_thread.start()
    speed_plotter.run_animation()  # Keep plotting on the main thread
    spin_thread.join()  # Wait for the ROS node thread to finish
    speed_plotter.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
