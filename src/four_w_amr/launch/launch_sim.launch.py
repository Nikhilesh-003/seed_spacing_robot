import os
from ament_index_python.packages import get_package_share_directory,get_package_prefix
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription,SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    package_name = 'four_w_amr'

    nina_description = "four_w_amr"
    nina_description_prefix = "four_w_amr"

    model_path = os.path.join(nina_description, "models")
    model_path += os.pathsep + os.path.join(nina_description_prefix, "share")

    env_var = SetEnvironmentVariable("GAZEBO_MODEL_PATH", model_path)

    
    # Include your custom launch file (rsp.launch.py)
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'rsp.launch.py'
        )]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Path to your Gazebo world file
    # world_file_path = os.path.join(get_package_share_directory(package_name), 'world', 'empty.world')

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        #launch_arguments={'world': world_file_path}.items()  # Pass the world file as an argument
    )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'my_bot'],
        output='screen'
    )

    # rviz = Node(
    #     package='rviz2',
    #     executable='rviz2',
    #     name='rviz2',
    # )
    
  
    # RTAB-Map ROS Node
    # rtabmap_ros_node = Node(
    #     package='rtabmap_slam',
    #     executable='rtabmap',
    #     name='rtabmap_ros',
    #     parameters=[
    #         # Add any RTAB-Map parameters here
    #         {'use_sim_time': True}  # Example parameter
    #     ],
    #     output='screen'
    # )





    # Launch them all!
    return LaunchDescription([rsp, gazebo, spawn_entity,env_var
                                  
                               ])
