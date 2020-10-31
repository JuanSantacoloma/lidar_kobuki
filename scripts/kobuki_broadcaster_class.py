#!/usr/bin/python

import rospy

import numpy as np
from   rospy.numpy_msg import numpy_msg
from tf.transformations import rotation_matrix 

import tf2_ros
import tf_conversions

from geometry_msgs.msg import TransformStamped
from ar_track_alvar_msgs.msg import AlvarMarkers, AlvarMarker

class Broadcaster:
    
    def __init__(self):
        
        # Para realizar la escucha "listener"
        self.tfBuffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tfBuffer)
        

        # Subscribers
        # rospy.Subscriber("/trajectory_marker", numpy_msg(AlvarMarkers), self.Marker_Callback, queue_size=10 )
        # self.Marker_Callback
    #--------------------------------------------------------------------------------------#
    # Callback o interrupcion
    def Marker_Callback(self):
        
        try:
            trans_mobbase_cam = self.tfBuffer.lookup_transform("base_link", "carrot1", rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.logwarn("Error trying to look for transform") 

        # Traslation x y
        quat_odom_cam = np.array([trans_mobbase_cam.transform.translation.x, \
                                    trans_mobbase_cam.transform.translation.y])
        # print(quat_odom_cam)
        return quat_odom_cam