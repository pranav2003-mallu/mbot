import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('mbot_description')
    joy_config = os.path.join(pkg_share, 'config', 'joystick.yaml')

    return LaunchDescription([
        # Joy Node - Reads raw gamepad inputs
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[joy_config],
            output='screen'
        ),

        # Teleop Twist Joy Node - Converts raw inputs into /cmd_vel messages
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_twist_joy_node',
            parameters=[joy_config],
            remappings=[('/cmd_vel', '/cmd_vel')],
            output='screen'
        )
    ])
