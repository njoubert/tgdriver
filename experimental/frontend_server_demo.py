import flask
import math
import time

app = flask.Flask(__name__)

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
<!--   <Placemark id="tg_dancefloor">
    <name>TechnoGecko DanceFloor</name>
      <Point>
        <coordinates>-95.43,40.42,0</coordinates>
      </Point>
  </Placemark> -->
</Document>
</kml>"""


LAT = 40.782609
LNG = -119.206641
RADIUS_LAT = 9e-4
RADIUS_LNG = 1e-3
START_TIME = time.time()
HEADING_OFFSET_DEG = 240

@app.route('/tg.kml')
def position():
    elapsed = START_TIME - time.time()
    theta = -(2 * math.pi / 60) * elapsed
    lat = LAT + RADIUS_LAT * math.sin(theta)
    lng = LNG + RADIUS_LNG * math.cos(theta)
    return POSE_TEMPLATE.format(lat=lat, lng=lng,
        heading=HEADING_OFFSET_DEG + math.degrees(-theta))
