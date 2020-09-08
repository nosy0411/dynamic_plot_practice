import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class DynamicUpdate:

    def on_launch(self):
        plt.ion()
        self.figure, self.ax = plt.subplots()
        # 초기 축 범위 설정
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 200)
        self.ax.grid(True)
        # 축은 값이 업데이트 됨에 따라 변경됨
        self.ax.set_autoscale_on(True)

    def on_running(self, xdata, ydata):

        self.ax.scatter(xdata, ydata, color='b')
        self.figure.canvas.draw()

    def callback(self, t, brightness):

        import time

        self.on_running(t, brightness)

        time.sleep(0.001)

        return t, brightness


if __name__ == '__main__':

    d = DynamicUpdate()
    d.on_launch()

    time = 0
    brightness = 0

    for i in range(10000):

        time = time + 0.5
        brightness = brightness + 0.01

        d.callback(time, brightness)
