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

def write_F(turtle_api):
    #narysowanie górnej poziomej linii
    targetx = 0 + 14
    targety = 10 + 20
    while (turtle_api.getPose('turtle1').x >= targetx):
        movement = Twist()
        movement.linear.x = -2.0
        movement.linear.y = 0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

    #narysowanie pionowej linii do połowy
    targetx = 0 + 14
    targety = 5 + 20
    while (turtle_api.getPose('turtle1').y >= targety):
        movement = Twist()
        movement.linear.x = 0
        movement.linear.y = -2.0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

    #narysowanie poziomej linii w połowie, ta linia jest krótsza od tej górnej
    targetx = 4 + 14
    targety = 5 + 20
    while (turtle_api.getPose('turtle1').x <= targetx):
        movement = Twist()
        movement.linear.x = 2.0
        movement.linear.y = 0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

    #powrót do poprzedniego punktu, aby dokończyć pionową linię
    targetx = 0 + 14
    targety = 5 + 20
    while (turtle_api.getPose('turtle1').x >= targetx):
        movement = Twist()
        movement.linear.x = -2.0
        movement.linear.y = 0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

    #narysowanie pionowej linii do końca w dół
    targetx = 0 + 14
    targety = 0 + 20
    while (turtle_api.getPose('turtle1').y >= targety):
        movement = Twist()
        movement.linear.x = 0
        movement.linear.y = -2.0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

def go_to_s(turtle_api):
    #przejście kawałek w prawo, aby móc narysować obok literę s
    targetx = 8 + 14
    targety = 0 + 20
    while (turtle_api.getPose('turtle1').x <= targetx):
        movement = Twist()
        movement.linear.x = 2.0
        movement.linear.y = 0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

def write_s(turtle_api):
    #narysowanie dolnej poziomej lini
    targetx = 15 + 14
    targety = 0 + 20
    while (turtle_api.getPose('turtle1').x <= targetx):
        movement = Twist()
        movement.linear.x = 2.0
        movement.linear.y = 0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

    #narysowanie linni idącej do połowy litery pionowo w góre
    targetx = 15 + 14
    targety = 3.5 + 20
    while (turtle_api.getPose('turtle1').y <= targety):
        movement = Twist()
        movement.linear.x = 0
        movement.linear.y = 2.0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

    #narysowanie poziomej linni w połowie litery s
    targetx = 8 + 14
    targety = 3.5 + 20
    while (turtle_api.getPose('turtle1').x >= targetx):
        movement = Twist()
        movement.linear.x = -2.0
        movement.linear.y = 0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

    #narysowanie linni pionowo do góry
    targetx = 8 + 14
    targety = 7 + 20
    while (turtle_api.getPose('turtle1').y <= targety):
        movement = Twist()
        movement.linear.x = 0
        movement.linear.y = 2.0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

    #narysowanie górnej poziomej linii
    targetx = 15 + 14
    targety = 7 + 20
    while (turtle_api.getPose('turtle1').x <= targetx):
        movement = Twist()
        movement.linear.x = 2.0
        movement.linear.y = 0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

def go_to_v(turtle_api):
    #przejście kawałek w prawo, aby zrobić odstęp między literami
    targetx = 16 + 14
    targety = 7 + 20
    while (turtle_api.getPose('turtle1').x <= targetx):
        movement = Twist()
        movement.linear.x = 2.0
        movement.linear.y = 0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

def write_v(turtle_api):
    #narysowanie lewej połowy litery v
    targetx = 19.5 + 14
    targety = 0 + 20
    while (turtle_api.getPose('turtle1').x <= targetx) or (turtle_api.getPose('turtle1').y >= targety):
        movement = Twist()
        movement.linear.x = 1.0
        movement.linear.y = -2.0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

    #narysowanie prawej połowy litery v
    targetx = 21 + 14
    targety = 5 + 20
    while (turtle_api.getPose('turtle1').x <= targetx) or (turtle_api.getPose('turtle1').y <= targety):
        movement = Twist()
        movement.linear.x = 1.0
        movement.linear.y = 2.0
        movement.angular.z = 0
        turtle_api.setVel("turtle1", movement)
        print_pos(turtle_api)

def print_pos(turtle_api):
    #wyświetlanie pozycji żółwia
    print ('POSE:')
    print ('\t {}',turtle_api.getPose('turtle1').x)
    print ('\t {}',turtle_api.getPose('turtle1').y)
    print ('\t {}',turtle_api.getPose('turtle1').theta)
    print( '\t {}',turtle_api.getPose('turtle1').linear_velocity)
    print( '\t {}',turtle_api.getPose('turtle1').angular_velocity)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    rospy.init_node('siu_example', anonymous=False)
    turtle_api = TurtlesimSIU.TurtlesimSIU()
    rate = rospy.Rate(10)
    if turtle_api.hasTurtle('turtle1'):
        turtle_api.killTurtle('turtle1')
    if not turtle_api.hasTurtle('turtle1'):
        # ustawiam żółwia (dodaje 14 do x i 15 do y, aby całość rysunku była w miarę na środku ekranu)
        # żółw jest obrócony głową w prawo
        turtle_api.spawnTurtle('turtle1',turtlesim.msg.Pose(x=7+14,y=10+20,theta=0))
    color_api = TurtlesimSIU.ColorSensor('turtle1')
    print(turtle_api.pixelsToScale())
    print_pos(turtle_api)

    #ustawienie pisaka na czerwony o grubości 20 i narysowanie litery F o wymiarach 10x10
    set_pen_req = turtlesim.srv.SetPenRequest(r=255, g=0, b=0, width=20, off=0)
    turtle_api.setPen('turtle1', set_pen_req)
    write_F(turtle_api)

    #podniesienie pisaka i przejście o metr w prawo - ustawienie żółwia do rysowania litery s
    set_pen_req = turtlesim.srv.SetPenRequest(r=0, g=0, b=0, width=5, off=1)
    turtle_api.setPen('turtle1', set_pen_req)
    go_to_s(turtle_api)

    #ustawienie pisaka na zielony o grubości 5 i narysowaie litery s
    #z racji, że litera s ma być mała to zdecydowałem się ją narysować w wymiarach 7x7
    set_pen_req = turtlesim.srv.SetPenRequest(r=0, g=255, b=0, width=5, off=0)
    turtle_api.setPen('turtle1', set_pen_req)
    write_s(turtle_api)

    #podniesienie pisaka i przejście o metr w prawo - ustawienie żółwia do rysowania litery s
    set_pen_req = turtlesim.srv.SetPenRequest(r=0, g=0, b=0, width=5, off=1)
    turtle_api.setPen('turtle1', set_pen_req)
    go_to_v(turtle_api)

    #ustawienie pisaka na niebieski o grubości 10 i narysowaie litery v
    #ponieważ litera v również ma być mała to narysowałem ją tak samo jak litere s w wymiarach 7x7
    set_pen_req = turtlesim.srv.SetPenRequest(r=0, g=0, b=255, width=10, off=0)
    turtle_api.setPen('turtle1', set_pen_req)
    write_v(turtle_api)


if __name__ == "__main__":
    main()