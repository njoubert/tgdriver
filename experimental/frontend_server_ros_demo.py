#!/usr/bin/env python

import flask
import math
import rospy
from piksi_rtk_msgs import msg
import time
import threading

POSE_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2"
     xmlns:gx="http://www.google.com/kml/ext/2.2">
    <Document>
      <Style id="gecko_icon">
        <IconStyle>
          <scale>5</scale>
          <heading>{heading}</heading>
          <Icon>
            <href>file://home/gecko/shared/gecko_icon.png</href>
          </Icon>
        </IconStyle>
      </Style>
      <Placemark id="tg_robot">
        <name>TechnoGecko Robot</name>
        <styleUrl>#gecko_icon</styleUrl>
        <Point>
          <coordinates>{lng},{lat},0</coordinates>
        </Point>
      </Placemark>
    </Document>
    </kml>"""

HEADING_OFFSET_DEG = 100

class GuardedPose(object):
  def __init__(self):
    self._pose_lock = threading.Lock()
    self._lat = 0
    self._lng = 0
    self._heading = 0

  def set_latlng(lat, lng):
    with self._pose_lock:
      self._lat, self._lng = lat, lng

  def set_heading(self, heading):
    with self._pose_lock:
      self._heading = heading

  def get():
    with self._pose_lock:
      return self._lat, self._lng, self._heading


guarded_pose = GuardedPose()

def gps_reader():
    rospy.init_node('gps_subscriber')
    position_sub = rospy.Subscriber('/gps_position/baseline_ned', msg.BaselineNed,
                                    position_callback)
    heading_sub = rospy.Subscriber('/gps_position/baseline_heading', msg.BaselineHeading,
                                    heading_callback)
    # rospy.spin()


@app.route('/tg.kml')
def position():
  global guarded_pose
  lat, lng = guarded_pose.get()
  return POSE_TEMPLATE.format(lat=lat, lng=lng,
                            heading=HEADING_OFFSET_DEG + math.degrees(theta))

def position_callback(m):
  global guarded_pose
  print "Position callback invoked."
  guarded_pose.set_latlng(m.lat, m.lng)

def heading_callback(m):
  global guarded_pose
  print "Heading callback invoked."
  guarded_pose.set_headinglng(m.heading)

def main():
    print('Starting GPS subscriber...')
    threading.Thread(target=gps_reader).start()

    print('Starting frontend server...')
    app = flask.Flask(__name__)
    app.run(host='localhost', port=9090)

if __name__ == '__main__':
    main()
