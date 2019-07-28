#!/usr/bin/env python

import rospy
from piksi_rtk_msgs import msg

def callback(m):
    print "north: {} east: {}".format(m.n, m.e)

rospy.init_node('gps_subscriber')
sub = rospy.Subscriber('/gps_position/baseline_ned', msg.BaselineNed, callback)
rospy.spin()
