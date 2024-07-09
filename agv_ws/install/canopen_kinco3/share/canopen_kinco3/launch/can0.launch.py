import os
from typing import Final, List

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import PushRosNamespace
from launch.conditions import LaunchConfigurationEquals

# Packages
CAN_CONFIG_PKG: Final[str] = "canopen_kinco3"
CAN_CORE_PKG: Final[str] = "canopen_core"
CAN_PROXY_PKG: Final[str] = "canopen_fake_slaves"

# Dirs
CAN0_CONFIG_DIR: Final[str] = "config/can0"
LAUNCH_DIR: Final[str] = "launch"

# File Paths
master_config_path = os.path.join(
    get_package_share_directory(CAN_CONFIG_PKG), CAN0_CONFIG_DIR, "master.dcf"
)

bus_config_path = os.path.join(
    get_package_share_directory(CAN_CONFIG_PKG), CAN0_CONFIG_DIR, "bus.yml"
)

eds_path = os.path.join(
    get_package_share_directory(CAN_CONFIG_PKG), CAN0_CONFIG_DIR, "KincoCMDriver.eds"
)

canopen_launch_path = os.path.join(
    get_package_share_directory(CAN_CORE_PKG), LAUNCH_DIR, "canopen.launch.py"
)

proxy_launch_path = os.path.join(
    get_package_share_directory(CAN_PROXY_PKG), LAUNCH_DIR, "basic_slave.launch.py"
)

# Launch Arguments
ARGUMENTS: List[DeclareLaunchArgument] = [
    DeclareLaunchArgument(
        name="namespace",
        default_value="",
        description="Namespace",
    ),
    DeclareLaunchArgument(
        name="canbus",
        default_value="vcan0",
        choices=["vcan0", "can0"],
        description="CAN bus to communicate on",
    ),
]


def generate_launch_description() -> LaunchDescription:
    """Generate launch description for CAN0 CAN communication nodes."""
    ld = LaunchDescription(ARGUMENTS)

    device_container = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(canopen_launch_path),
        launch_arguments={
            "master_config": master_config_path,
            "master_bin": "",
            "bus_config": bus_config_path,
            "can_interface_name": LaunchConfiguration("canbus"),
        }.items(),
    )

    can0_com_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(proxy_launch_path),
        launch_arguments={
            "node_id": "6",
            "node_name": "can0_com_node",
            "slave_config": eds_path,
        }.items(),
        condition=LaunchConfigurationEquals("canbus", "vcan0"),
    )

    # TODO: This does not namespace the master and proxy nodes and I can't figure out
    #       how to get them inside the namespace. I've opened a ticket for answers
    #       https://github.com/ros-industrial/ros2_canopen/issues/262
    can0_nodes_with_namespace = GroupAction(
        actions=[
            PushRosNamespace(LaunchConfiguration("namespace")),
            can0_com_node,
            device_container,
        ]
    )

    ld.add_action(can0_nodes_with_namespace)

    return ld
