#! /usr/bin/env python
import roslib
roslib.load_manifest('tum_ardrone')
import rospy
import actionlib

from tum_ardrone.msg import *

if __name__ == '__main__':
    rospy.init_node('send_commands')
    client = actionlib.SimpleActionClient('drone_autopilot/autoInit',AutoInitAction)
    client.wait_for_server()

    goal = AutoInitGoal()
    # Fill in the goal here
    goal.moveTime=500
    goal.initSpeed=0.5
    goal.riseTime=4000
    goal.waitTime=800
    client.send_goal(goal)
    state=client.wait_for_result(rospy.Duration.from_sec(5.0))
    print state
