#!/usr/bin/env python

import rospy
import math
from piksi_rtk_msgs import msg

rospy.init_node('gps_publisher')
pub = rospy.Publisher('/gps_position/baseline_ned', msg.BaselineNed)
rate = rospy.Rate(5)

theta = 0
ned = msg.BaselineNed()
ned.n = 0
ned.e = 0
while not rospy.is_shutdown():
  ned.n = math.sin(theta) * 1000
  ned.e = math.cos(theta) * 1000
  theta += 0.01
  pub.publish(ned)
  rate.sleep()
