# !/usr/bin/env python3
import rospy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from std_msgs.msg import Float32

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

subscriber = rospy.Subscriber("/led_brightness", Float32, self.callback)


def animate(i):
    ydata = []
    ydata.append(i)
    line.set_ydata(ydata)
    return line,


def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,


ani = animation.FuncAnimation(fig, animate, np.arange(
    1, 200), init_func=init, interval=25, blit=True)

plt.show()
