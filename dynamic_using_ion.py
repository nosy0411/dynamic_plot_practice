# 동적 그래프를 그리는 법은 크게 2가지가 있는데
# (1) plt.ion() 을 이용하는 방법
# (2) import matplotlib.animation as animation 즉 animation을 이용하는 방법


# set_xdata()와 set_ydata()로 변수x와y를 업데이트 한 다음
# canvas.draw()를 사용하여 애니메이션을 통해 업데이트를 표시함으로써 플롯을 실시간으로 업데이트 할 수 있습니다.
# 자바 스크립트 기반의 메소드.

# Matplotlib에서 플롯 업데이트를 자동화하기 위해 데이터를 업데이트하고
# 기존 플롯을 지우고 업데이트 된 데이터를 루프로 플롯
# 기존 플롯을 지우려면 canvas.draw(),canvas_flush_events(),
# plt.draw()및clear_output()과 같은 몇 가지 메서드를 사용

import numpy as np
import time
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.cos(x)

# plt.ion()은 대화식 모드를 켭니다. 플롯이 호출되지 않으면 플롯이 업데이트되지 않습니다.
plt.ion()

figure, ax = plt.subplots(figsize=(8, 6))
line1, = ax.plot(x, y)

plt.title("Dynamic Plot of sinx", fontsize=25)

plt.xlabel("X", fontsize=18)
plt.ylabel("sinX", fontsize=18)

for p in range(100):
    updated_y = np.cos(x-0.05*p)

    line1.set_xdata(x)
    line1.set_ydata(updated_y)

    # canvas.draw()는 그림을 표시하는 자바 스크립트 기반의 방법
    figure.canvas.draw()

    # canvas.flush_events()는 자바 스크립트 기반의 메소드로,
    # 모든 반복에서 숫자를 지우므로 연속 숫자가 겹치지 않을 수 있습니다.
    # figure.canvas.flush_events()
    time.sleep(0.1)

# 애니메이션이 끝나도 창을 열어두는 프로세스
plt.waitforbuttonpress()

# fig.clear()를 사용해서 지울 수도 있음
# for p in range(50):
#     p=3
#     updated_x=x+p
#     updated_y=np.cos(x)
#     plt.plot(updated_x,updated_y)
#     plt.draw()
#     x=updated_x
#     y=updated_y
#     plt.pause(0.2)
#     fig.clear()


# plt.clf를 이용해서 지울 수도 있음
# import matplotlib.pyplot as plt
# from time import sleep
# from random import shuffle

# plt.ion()

# y = [i for i in range(100)]
# x = [i for i in range(len(y))]

# for i in range(50): # 50 회 반복한다.
#     plt.clf()       # 그래프를 초기화한다.
#     plt.bar(x,y)    # 막대 그래프를 그린다.
#     plt.show()      # 막개 그래프를 화면에 표시한다.
#     sleep(0.5)      # 0.5초 프로그램 실행을  멈춘다.
#     shuffle(y)      # 데이터를 뒤섞는다.
