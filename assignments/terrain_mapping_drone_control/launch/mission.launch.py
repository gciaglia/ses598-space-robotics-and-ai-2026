from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    home_dir = os.environ['HOME']

    #GMB: Updating the path below since I am working out of a specific folder, and a ros ws specificall for this assignment
    base_path = os.path.join(home_dir, 'Desktop', 'SES598', 'HW_3','ros2_ws', 'src', 'terrain_mapping_drone_control', 'terrain_mapping_drone_control')

    return LaunchDescription([
        # Run aruco_tracker.py with log-level WARN to hush output
        ExecuteProcess(
            cmd=[
                'python3', os.path.join(base_path, 'aruco_tracker.py'),
                '--ros-args', '--log-level', 'warn'
            ],
            output='log',  # suppresses logs to log file instead of screen
        ),

        # Run auto_detect_land.py with screen output
        ExecuteProcess(
            cmd=['python3', os.path.join(base_path, 'auto_detect_land.py')],
            output='screen',
        )
    ])
