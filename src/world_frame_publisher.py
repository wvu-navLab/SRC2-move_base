#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
from nav_msgs.msg import Odometry
import tf
import sys


class WorldTruePosition():
    def __init__(self):

        rospy.init_node("world_true_position",anonymous=True)
        self.br = tf.TransformBroadcaster()
        rospy.loginfo("world_true_position publisher node is on")
        rospy.loginfo("and modified True odometry")
      #  self.r = rospy.Rate(20)
	self.pub = rospy.Publisher('/odom', Odometry, queue_size = 1)
        rospy.on_shutdown(self.shutdown)
        self.publish()

    def publish(self):
        while not rospy.is_shutdown():
            self.msg = rospy.wait_for_message("/odometry/truth", Odometry)
	    self.msg.twist.twist.linear.x = np.sqrt(np.square(self.msg.twist.twist.linear.x)+np.square(self.msg.twist.twist.linear.y))
	    #self.msg.twist.twist.linear.y = abs()
	    #self.msg.twist.twist.linear.z = 0.0
	    #self.msg.twist.twist.angular.x = 0.0
	    #self.msg.twist.twist.angular.y = 0.0
	    self.pub.publish(self.msg)
            self.msg.header.frame_id = "odom"
	    print(self.msg)
	    self.br.sendTransform((self.msg.pose.pose.position.x,self.msg.pose.pose.position.y,self.msg.pose.pose.position.z),
					(self.msg.pose.pose.orientation.x,self.msg.pose.pose.orientation.y,
					self.msg.pose.pose.orientation.z,self.msg.pose.pose.orientation.w),
					rospy.Time.now(),"scout_1_tf/base_footprint","odom")
	    self.br.sendTransform((0.0,0.0,0.0),
					(0.0,0.0,
					0.0,1.0),
					rospy.Time.now(),"odom","world")


    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("world_true_position Node is shutdown")
        rospy.sleep(1)

def main():
    try:
        world_true_position = WorldTruePosition()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()
