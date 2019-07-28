import sys

# QT imports
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

# ROS imports
import rospy
from std_msgs.msg import Int32

def gps_callback(msg):
    pass

class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.title = 'TechnoGecko Playa Viewer'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('brcmap.jpg')
        pixmap = pixmap.scaled(1000, 800, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

