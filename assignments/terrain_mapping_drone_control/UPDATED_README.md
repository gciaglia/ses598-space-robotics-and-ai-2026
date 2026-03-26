# Key Issues Expereinced:
The drone falls off the cylinder, the first cylinder is not detected as a repeat measurement, the battery SOC does not change.

## Setting PX4
```bash
git clone https://github.com/PX4/PX4-Autopilot.git
cd PX4-Autopilot
git checkout 9ac03f03eb
bash Tools/setup/ubuntu.sh
```


## Ground Control

This is needed to arm the Drone and allow it to take off. This is only checked once.

https://docs.qgroundcontrol.com/master/en/qgc-user-guide/getting_started/download_and_install.html
https://github.com/mavlink/qgroundcontrol/releases

# Commands/Run Process:

Terminal 1: Launch the Gazebo Simulation
```bash
cd ~/Desktop/SES598/HW_3/ros2_ws
colcon build --packages-select terrain_mapping_drone_control --symlink-install


cd ~/Desktop/SES598/HW_3/ros2_ws && source install/setup.bash
ros2 launch terrain_mapping_drone_control cylinder_landing.launch.py
```

Terminal 2: Setup PX4, allows PX4 messages to be translated to ROS2 topics
```bash
/snap/bin/micro-xrce-dds-agent udp4 -p 8888
```

Terminal 3: Run the mission, launch aruco_tracker and the auto_detect_land
```bash
cd ~/Desktop/SES598/HW_3/ros2_ws && source install/setup.bash
ros2 launch terrain_mapping_drone_control mission.launch.py
```

Terminal 4: Start Ground Control (This needs to be completed before mission starts or it will not arm)
```bash
./QGroundControl.AppImage
```
    -> To download ground control:
    ```bash
        cd ~/Desktop/SES598/HW_3
        wget https://github.com/mavlink/qgroundcontrol/releases/download/v4.4.3/QGroundControl.AppImage
        chmod +x QGroundControl.AppImage
        sudo apt install libfuse2
    ```

# Extra Credit
ros2 launch terrain_mapping_drone_control cylinder_mapping.launch.py

