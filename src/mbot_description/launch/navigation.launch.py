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
    nav2_launch_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')

    # Arguments
    sim_arg = DeclareLaunchArgument('sim', default_value='False')
    map_yaml = LaunchConfiguration('map')  
    lidar_port = LaunchConfiguration('lidar_port')
    serial_port = LaunchConfiguration('serial_port')
    use_rviz = LaunchConfiguration('use_rviz')
    use_sim_time = LaunchConfiguration('sim')

    xacro_file = os.path.join(pkg_share, 'urdf', 'mbot.xacro')
    nav2_params = os.path.join(pkg_share, 'config', 'nav2_params.yaml')
    rviz_config_path = os.path.join(pkg_share, 'rviz', 'rviz.rviz')

    robot_desc = ParameterValue(Command(['xacro ', xacro_file]), value_type=str)

    return LaunchDescription([
        sim_arg,
        DeclareLaunchArgument('map', description='Full path to map yaml file to load'),
        DeclareLaunchArgument('lidar_port', default_value='/dev/ttyUSB1'),
        DeclareLaunchArgument('serial_port', default_value='/dev/ttyUSB0'),
        DeclareLaunchArgument('use_rviz', default_value='True'),

        # 1. Robot State, Joints, & Transforms
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc, 'use_sim_time': use_sim_time}]
        ),

        # 2. Hardware Bridge (Only if NOT sim)
        Node(
            package='mbot_description',
            executable='robot_bridge.py',
            parameters=[{'port_name': serial_port}],
            condition=UnlessCondition(use_sim_time)
        ),

        # 3. RPLidar (Only if NOT sim)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(rplidar_pkg, 'launch', 'rplidar_a1_launch.py')),
            launch_arguments={'serial_port': lidar_port, 'frame_id': 'lidar_1'}.items(),
            condition=UnlessCondition(use_sim_time)
        ),

        # 5. Nav2 Bringup
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(nav2_launch_dir, 'bringup_launch.py')),
            launch_arguments={
                'map': map_yaml,
                'use_sim_time': use_sim_time,
                'params_file': nav2_params,
                'autostart': 'True'
            }.items()
        ),

        # 6. RViz2 (GUI Controllable)
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_path],
            condition=IfCondition(use_rviz),
            parameters=[{'use_sim_time': use_sim_time}]
        )
    ])
