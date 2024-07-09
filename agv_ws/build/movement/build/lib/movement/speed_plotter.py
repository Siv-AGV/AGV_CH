#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue
import time

def plot_process(q):
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    line_speeds_L, = ax.plot([], [], 'r-', label='Left Wheel Speed (rad/s)')
    line_speeds_R, = ax.plot([], [], 'b-', label='Right Wheel Speed (rad/s)')
    ax.set_xlabel('Traveled Distance (m)')
    ax.set_ylabel('Wheel Speeds (rad/s)')
    ax.legend()
    ax.grid(True)

    speeds_L = []
    speeds_R = []
    distances = []

    while True:
        while not q.empty():
            message = q.get()
            if message == "exit":
                plt.close('all')
                return
            distances.append(message['distance'])
            speeds_L.append(message['speed_L'])
            speeds_R.append(message['speed_R'])

        if distances:
            line_speeds_L.set_data(distances, speeds_L)
            line_speeds_R.set_data(distances, speeds_R)
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw()
            fig.canvas.flush_events()
        time.sleep(0.1)

class PlotterNode(Node):
    def __init__(self, q):
        super().__init__('data_plotter')
        self.q = q
        self.create_subscription(Float64MultiArray, 'wheel_speeds', self.listener_callback_speeds, 10)
        self.create_subscription(Float64, 'traveled_dist', self.listener_callback_distance, 10)
        self.speeds = []

    def listener_callback_speeds(self, msg):
        self.speeds = [msg.data[0], msg.data[1]]

    def listener_callback_distance(self, msg):
        if self.speeds:
            self.q.put({'distance': msg.data, 'speed_L': self.speeds[0], 'speed_R': self.speeds[1]})

def main(args=None):
    rclpy.init(args=args)
    q = Queue()
    plot_proc = Process(target=plot_process, args=(q,))
    plot_proc.start()
    plotter_node = PlotterNode(q)
    rclpy.spin(plotter_node)
    plotter_node.destroy_node()
    rclpy.shutdown()
    q.put("exit")
    plot_proc.join()

if __name__ == '__main__':
    main()
