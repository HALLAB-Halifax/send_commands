#!/usr/bin/env python
import roslib
roslib.load_manifest('tum_ardrone')
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point
import actionlib

from tum_ardrone.msg import *
def issue_commands(data):
    rospy.loginfo("waypoints: Got the target!!!")
    client = actionlib.SimpleActionClient('drone_autopilot/moveBy',MoveAction)
    client.wait_for_server()
    goal=MoveGoal()
    goal.x=data.x
    goal.y=data.y
    goal.z=data.z
    rospy.loginfo("waypoints: Sending goal")
    client.send_goal(goal)
    state=client.wait_for_result(rospy.Duration.from_sec(45.0))
    print state
    rospy.set_param('check',state)
    
   

  
	   
	   	
	  

if __name__ == '__main__':
    rospy.init_node('waypoints',anonymous=True)
    target=rospy.get_param("target","target")
    rospy.Subscriber(target,Point,issue_commands)
    rospy.spin()
    
    
    
        
