#!/usr/bin/env python3
#!coding=utf-8

from cgitb import reset
from glob import glob
from tracemalloc import start
import cv2
from cv2 import circle
from numpy import imag
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import Twist

global key_last 
key_last = 0
        
class SubscribeAndPublish:
    def __init__(self):

        self.__pub_ = rospy.Publisher("/cmd_vel",Twist,queue_size=1)
        self.__sub_ = rospy.Subscriber('camera/image_raw', Image, self.callback)

    def callback(self,data):
        global mouseX,mouseY,key_last
        cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.namedWindow('Aimbot')
        cv2.imshow('Aimbot', cv_img)
        move_cmd  = Twist()

        key = cv2.waitKey(1)

        if key_last != key and key != -1:
            key_last = key
        if(key == 119 or key_last == 119):
            move_cmd.linear.x = 0.99
        if(key == 97 or key_last == 97):
            move_cmd.angular.z = 0.99   
        if(key == 100 or key_last == 100):
            move_cmd.angular.z = -0.99   
        if(key == 120 or key_last == 120):
            move_cmd.linear.x = -0.99               
        
        self.__pub_.publish(move_cmd)
        if  key & 0xFF == 27:
            exit(0)

def main():
    rospy.init_node('Aimbot', anonymous=True)
    global bridge
    bridge = CvBridge()
    SubscribeAndPublish()
    rospy.spin()

if __name__ == "__main__":
    main()