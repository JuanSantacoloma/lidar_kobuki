#!/usr/bin/python

import rospy
from kobuki_broadcaster_class import Broadcaster

# Init of program
if __name__ == '__main__':

    rospy.init_node('kobuki_broadcaster', anonymous=True)

    rospy.loginfo("Node init")

    Broadcaster()

    rospy.spin()