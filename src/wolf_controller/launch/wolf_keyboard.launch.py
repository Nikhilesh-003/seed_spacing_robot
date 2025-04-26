import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    teleop_twist_keyboard = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_twist_keyboard',
        remappings=[
            ('/cmd_vel', '/diff_cont/cmd_vel_unstamped')
        ]
    )

    return LaunchDescription([
        teleop_twist_keyboard
    ])
