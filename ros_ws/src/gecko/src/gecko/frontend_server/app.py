#!/usr/bin/env python

import flask
import math
import rospy
from piksi_rtk_msgs.msg import BaselineHeading
from sensor_msgs.msg import NavSatFix
import time
import threading

PORT = int(rospy.get_param('/frontend_server/port'))
app = flask.Flask(__name__, static_url_path='/static')

POSE_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2"
     xmlns:gx="http://www.google.com/kml/ext/2.2">
    <Document>
      <Style id="gecko_icon">
        <IconStyle>
          <scale>5</scale>
          <heading>{heading}</heading>
          <Icon>
            <href>http://localhost:{port}/static/gecko_icon.png</href>
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

  def set_latlng(self, lat, lng):
    with self._pose_lock:
      self._lat, self._lng = lat, lng

  def set_heading(self, heading):
    with self._pose_lock:
      self._heading = heading

  def get(self):
    with self._pose_lock:
      return self._lat, self._lng, self._heading


guarded_pose = GuardedPose()

def gps_reader():
    rospy.init_node('gps_subscriber', disable_signals=True)
    position_sub = rospy.Subscriber('/gps_position/navsatfix_best_fix', NavSatFix,
                                    position_callback)
    heading_sub = rospy.Subscriber('/gps_position/baseline_heading', BaselineHeading,
                                    heading_callback)

@app.route('/tg.kml')
def position():
  global guarded_pose
  lat, lng, heading = guarded_pose.get()
  return POSE_TEMPLATE.format(port=PORT, lat=lat, lng=lng,
    heading=HEADING_OFFSET_DEG + math.degrees(heading))

def position_callback(m):
  global guarded_pose
  print "Position callback invoked."
  guarded_pose.set_latlng(m.latitude, m.longitude)

def heading_callback(m):
  global guarded_pose
  print "Heading callback invoked."
  guarded_pose.set_headinglng(m.heading)

def main():
    print('Starting GPS subscriber...')
    threading.Thread(target=gps_reader).start()

    print('Starting frontend server...')
    app.run(host='localhost', port=PORT)

if __name__ == '__main__':
    main()
