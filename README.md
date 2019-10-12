# ARTags
The AR Tags package for AIR LAB at WPI

## Setting up
Install the latest version of librealsense by following instructions on the librealsense repository: [librealsense](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md)

Create a catkin workspace and clone the realsense ROS wrapper: [realsense-ros](https://github.com/IntelRealSense/realsense-ros). 

Clone ddynamic as well as it is required for the newer versions of realsense-ros: [ddynamic_reconfigure](https://github.com/pal-robotics/ddynamic_reconfigure/tree/kinetic-devel)

Clone this repository into your catkin workspace and compile. 

Once compiled, source the workspace and connect the Intel RealSense camera and launch the rs_camera launch file
```
roslaunch realsense2_camera rs_camera.launch
```
Next launch the AR nodes using the following command:
```
roslaunch calibrate_camera track_alvar.launch
```

The transform to the AR tag detected will be published in the tf topic under the frame artags.

