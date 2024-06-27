#!/usr/bin/env python
# encoding: utf8
import rospy
import turtlesim
from turtlesim.msg import Pose
from turtlesim.srv import SetPenRequest
from TurtlesimSIU import TurtlesimSIU
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import math
import signal
import sys
import numpy as np

def signal_handler(sig, frame):
    print ("Terminating")
    sys.exit(0)

def write_c(turtle_api):
    targetx = 10
    targety = 20
    while (turtle_api.getPose('turtle1').y >= targety) or (turtle_api.getPose('turtle1').x >= targetx):
        movement = Twist()
        movement.linear.x = 2.0
        movement.linear.y = 1.0
        movement.angular.z = 0.8
        turtle_api.setVel("turtle1", movement)
        print ('POSE:')
        print ('\t {}',turtle_api.getPose('turtle1').x)
        print ('\t {}',turtle_api.getPose('turtle1').y)
        print ('\t {}',turtle_api.getPose('turtle1').theta)
        print( '\t {}',turtle_api.getPose('turtle1').linear_velocity)
        print( '\t {}',turtle_api.getPose('turtle1').angular_velocity)


def main():
    # Initialize ROS node
    signal.signal(signal.SIGINT, signal_handler)
    rospy.init_node('siu_example', anonymous=False)
    turtle_api = TurtlesimSIU.TurtlesimSIU()
    rate = rospy.Rate(10)
    set_pen_req = turtlesim.srv.SetPenRequest(r=255, g=255, b=255, width=5, off=0)
    #set_pen_req = turtlesim.srv.SetPenRequest(r=255, g=255, b=255, width=5, off=1)
    if turtle_api.hasTurtle('turtle1'):
        turtle_api.killTurtle('turtle1')
        # rospy.sleep(2)
    if not turtle_api.hasTurtle('turtle1'):
        turtle_api.spawnTurtle('turtle1',turtlesim.msg.Pose(x=10,y=30,theta=0))
    color_api = TurtlesimSIU.ColorSensor('turtle1')
    print (turtle_api.pixelsToScale())
    print ('POSE:')
    print ('\t {}',turtle_api.getPose('turtle1').x)
    print ('\t {}',turtle_api.getPose('turtle1').y)
    print ('\t {}',turtle_api.getPose('turtle1').theta)
    print( '\t {}',turtle_api.getPose('turtle1').linear_velocity)
    print( '\t {}',turtle_api.getPose('turtle1').angular_velocity)
    write_c(turtle_api)


if __name__ == "__main__":
    main()
