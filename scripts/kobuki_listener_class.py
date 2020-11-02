#!/usr/bin/python

import rospy

import numpy as np
from   rospy.numpy_msg import numpy_msg
from tf.transformations import rotation_matrix 
import math
import tf2_ros
import tf_conversions
import geometry_msgs.msg

class Listener:
    
    def __init__(self):

        # Topics
        self.topicPub = "/mobile_base/commands/velocity"
        # Para realizar la escucha "listener"
        self.tfBuffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tfBuffer)

        # Publisher
        self.kobuki_vel = rospy.Publisher(self.topicPub , geometry_msgs.msg.Twist, queue_size=1)
        #--------------------------------------------------------------------------------------#
        # Polling Velocity to kobuki/ Twist Msg
        rate = rospy.Rate(10.0)
        while not rospy.is_shutdown():
            try:
                trans = self.tfBuffer.lookup_transform('base_footprint', 'carrot1', rospy.Time())
            except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                rospy.logwarn("Error trying to look for transform")
                rate.sleep()
                continue

            msg = geometry_msgs.msg.Twist()

            msg.angular.z = 1.9 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)
            msg.linear.x = 0.05 * math.sqrt(trans.transform.translation.x ** 2 + trans.transform.translation.y ** 2)

            self.kobuki_vel.publish(msg)
    
    def calcMTH(self,marc1,marc2):
        # Polling Velocity to kobuki/ Twist Msg
        rate = rospy.Rate(10.0)
        while not rospy.is_shutdown():
            try:
                self.trans = self.tfBuffer.lookup_transform(marc1, marc2, rospy.Time())
            except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                rospy.logwarn("Error trying to look for transform")
                rate.sleep()
                continue

        return self.trans.transform.translation.x
            