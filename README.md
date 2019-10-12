# ARTags
The AR Tags package for AIR LAB at WPI

## Setting up
Install librealsense by following instructions from [here](https://github.com/IntelRealSense/librealsense)
Install ddynamic-reconfigure ROS package by using the following command

```
sudo apt install ros-kinetic-ddynamic-reconfigure
```

Clone the entire repository into your catkin workspace and compile. 

Once compiled, source the workspace. Then connect the Intel RealSense camera and launch the rs_camera launch file
```
roslaunch realsense2_camera rs_camera.launch
```
Next launch the AR nodes using the following command
```
roslaunch calibrate_camera track_alvar.launch
```

The transform to the AR tag detected will be published in the tf topic under the frame artags.

