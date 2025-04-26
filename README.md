**Seed Spacing Robot**

SOFTWARES USED:

> OS: Ubuntu 22.04 

> Framework: ROS2 Humble

> Add-ons: Open CV


HARDWARE USED:

![image](https://github.com/user-attachments/assets/c2887a2d-7948-4080-be45-bbc78053ef5f)


PACKAGES REQUIRED:
```bash
sudo apt install ros-humble-xacro
sudo apt install ros-humble-joint-state-publisher-gui
sudo apt install ros-humble-gazebo-ros-pkgs
```


LAUNCHING COMMANDS:

In Terminal 1: (To visualize the robot in rviz)
```bash
ros2 launch four_w_amr display.launch.py
```

![image](https://github.com/user-attachments/assets/d5583ebd-7960-4f23-9d19-04c22abc5081)


For Hardware:

It is recommended to clone this repo on the OBCs (Jetson / Raspberry Pi).

```bash
ros2 launch four_w_amr bringup.launch.py
```

This launch file loads the necessary hardware firmware and micro-ros for the robot to start.

To obtain data from 2D RP-Lidar used:
```bash
ros2 launch four_w_amr lidar.launch.py
```

To obtain data from Intel-D435 Depth used:
```bash
ros2 launch four_w_amr realsense.launch.py
```

To perform SLAM using 2D Lidar:
```bash
ros2 launch four_w_amr_nav2 slam.launch.py
```

To perform navigation, update the saved map and launch this file:
```bash
ros2 launch four_w_amr_nav2 navigation.launch.py
```

 ![image](https://github.com/user-attachments/assets/1ee97f16-2c84-49fc-915c-61d77cf37060)



