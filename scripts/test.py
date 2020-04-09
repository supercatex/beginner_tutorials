#!/usr/bin/python3
import cv2
import tensorflow as tf

import rospy


if __name__ == "__main__":
    rospy.init_node("beginner_tutorials_test", anonymous=True)
    rospy.loginfo("Node created.")

    print(cv2.getBuildInformation())
    print("Tensorflow GPU:", tf.test.is_gpu_available())
