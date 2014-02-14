#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point

def talker():
    pub = rospy.Publisher('target', Point)
    rospy.init_node('landing_pad', anonymous=True)
    r = rospy.Rate(10) # 10hz
    p=Point()
    p.x=320
    p.y=320
    p.z=0
    
    rospy.loginfo(p)
    pub.publish(p)
    r.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
