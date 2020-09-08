import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class DynamicUpdate:

    def on_launch(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()
        # 초기 축 범위 설정
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 200)
        self.ax.grid(True)
        # 축은 값이 업데이트 됨에 따라 변경됨
        self.ax.set_autoscale_on(True)

        # 초기화
        x = 0
        y = 0
        self.lines, = self.ax.plot(x, y)

    def on_running(self, xdata, ydata):

        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)

        self.ax.relim()
        self.ax.autoscale_view()

        self.fig.canvas.draw()

    def callback(self, t, brightness):

        import time

        xdata = t
        ydata = brightness

        self.on_running(xdata, ydata)

        time.sleep(0.1)

        return xdata, ydata


if __name__ == '__main__':

    d = DynamicUpdate()
    d.on_launch()

    time = 0
    brightness = 0

    t_list = [0]
    b_list = [0]

    for i in range(100):
        time = time + 0.5
        brightness = brightness + 0.01
        t_list.append(time)
        b_list.append(brightness)

        d.callback(t_list, b_list)
