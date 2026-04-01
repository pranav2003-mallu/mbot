import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    pkg_share = get_package_share_directory('mbot_description')
    serial_port = LaunchConfiguration('serial_port')

    xacro_file = os.path.join(pkg_share, 'urdf', 'mbot.xacro')
    rviz_config = os.path.join(pkg_share, 'rviz', 'rviz.rviz')

    robot_desc = ParameterValue(Command(['xacro ', xacro_file]), value_type=str)

    return LaunchDescription([
        DeclareLaunchArgument('serial_port', default_value='/dev/ttyUSB0', description='Bridge Serial Port'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}],
            output='screen'
        ),

        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            parameters=[{'robot_description': robot_desc}],
            output='screen'
        ),

        Node(
            package='mbot_description',
            executable='robot_bridge.py',
            name='robot_bridge',
            parameters=[{'port_name': serial_port}],
            output='screen'
        ),

        Node(
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard',
            name='keyboard_teleop',
            output='screen'
        ),
    ])
