#!/usr/bin/env python3
 
import rospy
from gazebo_msgs.srv import *
 
get_state_service = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
model = GetModelStateRequest()
model.model_name = 'robot'
objstate = get_state_service(model)
model2 = GetModelStateRequest()
model2.model_name = 'unit_box'
objstate2 = get_state_service(model2)
print(objstate.pose.position)
print('\n')
print(objstate2.pose.position)
state = (objstate.pose.position.x, objstate.pose.position.y, objstate.pose.position.z)