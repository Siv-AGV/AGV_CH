from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='agv_controller',  # Replace with your package name
            executable='wheel_controller.py',
            name='wheel_controller',
            respawn=True,  # Automatically restart the node if it shuts down
            respawn_delay=4,
        )
    ])
