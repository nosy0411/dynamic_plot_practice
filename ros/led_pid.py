#!/usr/bin/env python3
import rospy
import numpy as np
import time
from std_msgs.msg import Float32

class led_pid:

    def __init__(self, kp, ki, kd, ref):
        self.kp=kp
        self.ki=ki
        self.kd=kd
        self.ref=ref
        
        self.err_sum=0
        self.err_last=ref
        
        self.subscriber = rospy.Subscriber("/image_brightness",Float32,self.callback)
        self.publisher = rospy.Publisher("/led_brightness", Float32, queue_size=10)
        
    def callback(self, msg):
        rospy.loginfo("brightness : %d",msg.data)
        self.control(msg.data)
        rospy.loginfo("result %f",self.result)
        
        new_msg=Float32()
        new_msg.data=self.result
        self.publisher.publish(new_msg)
        
    def control(self,brightness):
        self.err=self.ref-brightness
        self.err_sum+=self.err
        self.err_dif=self.err-self.err_last
        
        self.result = self.kp*self.err + self.ki*self.err_sum + self.kd*(self.err_dif)
        self.err_last=self.err
        
        rospy.loginfo("control value : %f",self.result)
    
if __name__=='__main__':
    rospy.init_node('led_pid')
    led_pid(0.005,0.000,0,70)
    rospy.spin()
    














