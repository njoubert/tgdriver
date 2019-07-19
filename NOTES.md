# NOTES

## 2019-07-18

Run `tgops` `./provision_040_ros.sh`

reading  http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment

Create a ROS workspace in `tgdriver/ros_ws`

```
cd ~/Code/tgdriver
mkdir -p ros_ws/src
cd ros_ws
catkin_make
source devel/setup.bash
```
Check that install worked

```
echo $ROS_PACKAGE_PATH
```