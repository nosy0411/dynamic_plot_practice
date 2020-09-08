#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Float32
 
 
class Gray():
    def __init__(self):
        self.selecting_sub_image = "raw" # you can choose image type "compressed", "raw"
 
        if self.selecting_sub_image == "compressed":
            self._sub = rospy.Subscriber('/camera/image_raw/compressed', CompressedImage, self.callback, queue_size=1)
        else:
            self._sub = rospy.Subscriber('/camera/image_raw', Image, self.callback, queue_size=10)
        
        self.publisher = rospy.Publisher("/image_brightness", Float32, queue_size=10)
        
        self.bridge = CvBridge()
 
    def callback(self, image_msg):
 
        if self.selecting_sub_image == "compressed":
            #converting compressed image to opencv image
            np_arr = np.fromstring(image_msg.data, np.uint8)
            cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        elif self.selecting_sub_image == "raw":
            cv_image = self.bridge.imgmsg_to_cv2(image_msg, "bgr8")
 
        cv_gray = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)

        cv2.imshow('cv_gray', cv_gray), cv2.waitKey(1)
        
        height, width = cv_gray.shape
        
        brightness = np.sum(cv_gray) / (height * width)
        '''total=0
        for y in range(0,height):
            for x in range(0,width):
                total+=cv_gray[y,x]
        brightness = total/(height*width)'''
        
        rospy.loginfo("%d %d",height,width)
        
        new_msg=Float32()
        new_msg.data=brightness
        self.publisher.publish(new_msg)
        
    def main(self):
        rospy.spin()
 
if __name__ == '__main__':
    rospy.init_node('gray')
    node = Gray()
    node.main()

