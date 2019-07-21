# NOTES

## 2019-07-20

GOAL: Get GPS and LIDAR data sucked in.

Cheat Sheet:
```
catkin_make        - builds repo
rospack            - helps you find packages
	rospack find [package name]
roslaunch 
	roslaunch [package] [launchfile]

```

Let's install the `sick_scan` package to work with the LIDAR.
Following instructions in http://wiki.ros.org/sick_scan
in `~/Code/thdriver/ros_ws/src`:
```
git clone -b devel --single-branch git://github.com/SICKAG/sick_scan.git
cd ..
catkin_make
```

Edit the `tgdriver/ros_ws/src/sick_scan/launch/sick_lms_1xx.launch` file to point to `10.1.32.120`

`roslaunch sick_scan sick_lms_1xx.launch`

Alright, reading online: the `sick_scan` package does not support LMS111. Switching to ` lms1xx` package. From http://wiki.ros.org/LMS1xx

`sudo apt-get install ros-melodic-lms1xx`
Not found...

Build from source then
in `~/Code/thdriver/ros_ws/src`:
```

```

GIL ARRIVES

<debugging hell>

### Add LMS1xx as submodule
```
git submodule add https://github.com/clearpathrobotics/LMS1xx.git
```
It works with completely default settings on port 2111. `

## 2019-07-18: ROS Workspace Created

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

