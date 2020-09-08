#!/usr/bin/env python3
import rospy
import numpy as np
import time
import os
from std_msgs.msg import Float32
import matplotlib.pyplot as plt

path = "/home/rise/catkin_ws/src/ros_led_control/src/"



class led_pid:

    def __init__(self, kp, ki, kd, ref):
        self.kp=kp
        self.ki=ki
        self.kd=kd
        self.ref=ref
        
        self.err_sum=0
        self.err_last=ref

        # graph
        self.star_time = time.time()
        self.time1=0
        self.brightness=0
        self.brightness_msg=0
        self.result=0
        self.t_list=[]
        self.b_list=[]

        self.fig, self.ax = plt.subplots()
        # 초기 축 범위 설정
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 200)
        self.ax.grid(True)
        # 축은 업데이트 됨에 따라 변경됨
        self.ax.set_autoscale_on(True)

        x=0
        y=0
        # 초기화
        self.lines, = self.ax.plot(x, y)
        
        self.publisher = rospy.Publisher("/led_brightness", Float32, queue_size=10)

    def on_running(self):

        xdata = self.t_list
        ydata = self.b_list

        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)

        self.ax.relim()
        self.ax.autoscale_view()

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        
    def callback(self, msg):
        rospy.loginfo("brightness : %d",msg.data)
        self.control(msg.data)
        rospy.loginfo("result %f",self.result)

        self.brightness_msg = msg.data
        new_msg=Float32()
        new_msg.data=self.result
        self.publisher.publish(new_msg)

        d1 = time.time()
        d2 = d1-self.star_time
        self.star_time = d1

        self.brightness = self.result + self.brightness_msg
        self.time1 = self.time1 + d2
        self.t_list.append(self.time1)
        self.b_list.append(self.brightness)

        
    def control(self,brightness):
        self.err=self.ref-brightness
        self.err_sum+=self.err
        self.err_dif=self.err-self.err_last
        
        self.result = self.kp*self.err + self.ki*self.err_sum + self.kd*(self.err_dif)
        self.err_last=self.err
        
        rospy.loginfo("control value : %f",self.result)
    
if __name__=='__main__':
    
    os.chdir(path)
    plt.ion()

    start = time.time()
    finish = time.time()
    rospy.init_node('led_pid')
    d = led_pid(1.1,0.000,0,100)
    rospy.Subscriber("/image_brightness",Float32, d.callback)

    while True:
        d.on_running()
        finish = time.time()

        if (finish-start)>20:
            print("time out")
            plt.savefig("time_out.png")
            plt.close()
            break

        elif abs(d.brightness-d.ref)<0.05:

            plt.savefig("last_pic.png")
            plt.close()
            break
    rospy.spin()
    














