# Key Issues Expereinced:

## Setting PX4

## Ground Control

This is needed to arm the Drone and allow it to take off. This is only checked once.

https://docs.qgroundcontrol.com/master/en/qgc-user-guide/getting_started/download_and_install.html
https://github.com/mavlink/qgroundcontrol/releases

# Commands/Run Process:

Terminal 1: Launch the Gazebo Simulation

cd ~/Desktop/SES598/HW_3/ros2_ws && source install/setup.bash
ros2 launch terrain_mapping_drone_control cylinder_landing.launch.py


Terminal 2: Setup PX4, allows PX4 messages to be translated to ROS2 topics

/snap/bin/micro-xrce-dds-agent udp4 -p 8888


Terminal 3: Run the mission, launch aruco_tracker and the auto_detect_land

cd ~/Desktop/SES598/HW_3/ros2_ws && source install/setup.bash
ros2 launch terrain_mapping_drone_control mission.launch.py


Terminal 4: Start Ground Control


-> To download ground control:
    cd ~/Desktop/SES598/HW_3
wget https://github.com/mavlink/qgroundcontrol/releases/download/v4.4.3/QGroundControl.AppImage
chmod +x QGroundControl.AppImage
./QGroundControl.AppImage
sudo apt install libfuse2
