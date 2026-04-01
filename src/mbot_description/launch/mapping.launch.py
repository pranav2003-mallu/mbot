import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    pkg_share = get_package_share_directory('mbot_description')
    rplidar_pkg = get_package_share_directory('rplidar_ros')
    slam_pkg = get_package_share_directory('slam_toolbox')

    # Arguments
    sim_arg = DeclareLaunchArgument('sim', default_value='False')
    lidar_port = LaunchConfiguration('lidar_port')
    serial_port = LaunchConfiguration('serial_port')
    use_rviz = LaunchConfiguration('use_rviz')
    use_sim_time = LaunchConfiguration('sim')

    xacro_file = os.path.join(pkg_share, 'urdf', 'mbot.xacro')
    slam_params = os.path.join(pkg_share, 'config', 'mapper_params_online_async.yaml')
    rviz_config_path = os.path.join(pkg_share, 'rviz', 'rviz.rviz')

    robot_desc = ParameterValue(Command(['xacro ', xacro_file]), value_type=str)

    return LaunchDescription([
        sim_arg,
        DeclareLaunchArgument('lidar_port', default_value='/dev/ttyUSB1'),
        DeclareLaunchArgument('serial_port', default_value='/dev/ttyUSB0'),
        DeclareLaunchArgument('use_rviz', default_value='True'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc, 'use_sim_time': use_sim_time}]
        ),
        
        # 1. Hardware-only: Only launch Lidar and Bridge if NOT in simulation
        Node(
            package='mbot_description',
            executable='robot_bridge.py',
            parameters=[{'port_name': serial_port}],
            condition=UnlessCondition(use_sim_time)
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(rplidar_pkg, 'launch', 'rplidar_a1_launch.py')),
            launch_arguments={'serial_port': lidar_port, 'frame_id': 'lidar_1'}.items(),
            condition=UnlessCondition(use_sim_time)
        ),

        # 2. Mapping
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(slam_pkg, 'launch', 'online_async_launch.py')),
            launch_arguments={'slam_params_file': slam_params, 'use_sim_time': use_sim_time}.items()
        ),
        
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_path],
            condition=IfCondition(use_rviz),
            parameters=[{'use_sim_time': use_sim_time}]
        )
    ])
