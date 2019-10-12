#!/usr/bin/env python

import rospy
import tf
from visualization_msgs.msg import Marker



class AR_Transform_Publisher(object):
    def __init__(self):
        rospy.init_node('ar_transform_publisher')
        self.marker_sub = rospy.Subscriber('/visualization_marker', Marker, self.marker_callback)
        self.transform_publisher = tf.TransformBroadcaster()
        rospy.spin()
    def marker_callback(self, msg):
        parent_frame = msg.header.frame_id
        pos = msg.pose.position
        orient = msg.pose.orientation
        self.transform_publisher.sendTransform((pos.x, pos.y, pos.z), (orient.x, orient.y, orient.z, orient.w), 
                        rospy.Time.now(), "ar_tag", parent_frame)


if __name__ == '__main__':
    transform = AR_Transform_Publisher()