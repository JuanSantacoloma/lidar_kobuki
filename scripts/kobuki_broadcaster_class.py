#!/usr/bin/python

import rospy

import numpy as np
from   rospy.numpy_msg import numpy_msg
from tf.transformations import rotation_matrix 

import tf2_ros
import tf_conversions
from geometry_msgs.msg import TransformStamped
from kobuki_listener_class import Listener

class Broadcaster:
    
    def __init__(self):
        
        # Para realizar el "broadcast"
        self.broadcts  = tf2_ros.TransformBroadcaster()
        self.trans = TransformStamped()
        

        # It is needed to determine which task frame is the parent (base)
        # and the name of the new TF
        self.trans.header.frame_id = 'odom' # Parent or base frame
        self.trans.child_frame_id = 'carrot1'

        # Trajectory
        i=0
        trajecx = np.array([-3.5,-3.5, 1.5, 1.5, 3.5, 3.5,-2.5,-2.5, 1.5, 1.5,-1.0])
        trajecy = np.array([0,   3.5, 3.5,-1.5,-1.5,-8.0,-8.0,-5.5,-5.5,-3.5,-3.5])
        
        # Polling send trajectory
        rate = rospy.Rate(10.0)
        while not rospy.is_shutdown():
            
             # It is needed to stamp (associate a time) to the MTH
            self.trans.header.stamp = rospy.Time.now()
            
            # Values for the transformation (self.trans)
            self.trans.transform.translation.x = trajecx[i]
            self.trans.transform.translation.y = trajecy[i]
            self.trans.transform.translation.z = 0.0
            self.trans.transform.rotation.x = 0.0
            self.trans.transform.rotation.y = 0.0
            self.trans.transform.rotation.z = 0.0
            self.trans.transform.rotation.w = 1.0

            self.broadcts.sendTransform(self.trans)
            
            # self.listn = Listener()
            # a = self.listn.calcMTH('base_footprint','carrot1')
            # print(a)

    #--------------------------------------------------------------------------------------#
    # Callback o interrupcion
    # def Marker_Callback(self):
        
    #     try:
    #         trans_mobbase_cam = self.tfBuffer.lookup_transform("base_link", "carrot1", rospy.Time())
    #     except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
    #         rospy.logwarn("Error trying to look for transform") 
    #         return 0
    #     # Traslation x y
    #     quat_odom_cam = np.array([trans_mobbase_cam.transform.translation.x, \
    #                                 trans_mobbase_cam.transform.translation.y])
    #     # print(quat_odom_cam)
    #     return quat_odom_cam