import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    pkg_share = get_package_share_directory('mbot_description')
    gazebo_ros_share = get_package_share_directory('gazebo_ros')

    # Arguments
    gui_arg = DeclareLaunchArgument('gui', default_value='false', description='Launch Gazebo GUI')
    world_arg = DeclareLaunchArgument('world', 
                                      default_value=os.path.join(pkg_share, 'worlds', 'room.world'),
                                      description='Full path to world model file to load')

    xacro_file = os.path.join(pkg_share, 'urdf', 'mbot.xacro')
    robot_desc = ParameterValue(Command(['xacro ', xacro_file]), value_type=str)
    
    # Resolve package mesh paths for Gazebo to prevent Camera px!=0 crash
    install_dir = os.path.join(pkg_share, '..')

    return LaunchDescription([
        SetEnvironmentVariable(name='GAZEBO_MODEL_PATH', value=[
            os.environ.get('GAZEBO_MODEL_PATH', '') + ':' + install_dir if os.environ.get('GAZEBO_MODEL_PATH') else install_dir]),
            
        gui_arg,
        world_arg,

        # 1. Start Gazebo Server & Client using standard include
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(gazebo_ros_share, 'launch', 'gazebo.launch.py')),
            launch_arguments={
                'gui': LaunchConfiguration('gui'),
                'world': LaunchConfiguration('world')
            }.items()
        ),

        # 2. Publish Robot State
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
        ),

        # 3. Spawn Robot in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            output='screen',
            arguments=[
                '-entity', 'mbot',
                '-topic', 'robot_description',
                '-z', '0.2'
            ]
        ),
        
        # 4. Joint State Publisher
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            parameters=[{'use_sim_time': True}]
        ),
    ])
