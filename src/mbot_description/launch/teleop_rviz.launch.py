import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    pkg_share = get_package_share_directory('mbot_description')

    xacro_file = os.path.join(pkg_share, 'urdf', 'mbot.xacro')
    rviz_config = os.path.join(pkg_share, 'rviz', 'rviz.rviz')

    robot_desc = ParameterValue(
        Command(['xacro ', xacro_file]),
        value_type=str
    )

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}],
            output='screen'
        ),


        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            output='screen'
        ),


        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0','0','0','0','0','0','odom','base_footprint']
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0','0','0','0','0','0','base_footprint','base_link']
        ),

        Node(
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard',
            prefix='xterm -e',
            output='screen'
        ),
        
        Node(
            package='mbot_description',
            executable='fake_odom.py',
            output='screen'
        ),  


        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        ),
    ])
