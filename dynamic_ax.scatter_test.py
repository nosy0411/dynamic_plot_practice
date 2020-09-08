import numpy as np
import time
import matplotlib.pyplot as plt

# plt.ion()은 대화식 모드를 켭니다. 플롯이 호출되지 않으면 플롯이 업데이트되지 않습니다.
plt.ion()
fig, ax = plt.subplots()


# 초기 축 범위 설정. 초기 축 범위 제한이 없다면 scatter는 자동으로 축을 업데이트 해나감
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.grid(True)

# 범위를 설정해도 축 업데이트를 하는 법
# ax.axis('auto')
# set_autoscale_on은 축을 자동으로 업데이트 해줌
ax.set_autoscale_on(True)
# y축만 업데이트 하고 싶으면 set_autoscaley_on(True)
# x축만 업데이트 하고 싶으면 set_autoscalex_on(True)

x = 0
y = 0


for p in range(10000):
    x = x + 0.5
    y = y + 0.01

    # scatter 테스트
    # 일반 선 그래프 plot을 할 때는 lines, = ax.plot([],[]) 과 같이 해야함
    # scatter는 다양한 마커사이즈와 컬러를 사용하여 만든 플롯임
    # plot()도 마커만 보여주는 플롯이 가능하고 속도도 scatter에 비해 빠른편임
    # 그러나 scatter는 plot함수에서 제공하지 않는 높은 자유도를 제공하며 다양한 플롯을 그리는 것이 가능함
    # 따라서 속도냐 다양성이냐에 따라 사용자가 직접 선택하여 사용하면 됨
    line1 = ax.scatter(x, y)
    # ax.autoscale_view()

    fig.canvas.draw()

    # fig.canvas.flush_events()
    # scatter같은 경우 겹치는 경우가 없으니까 flush_events()를 안해줘도 됨

    time.sleep(0.001)

# 애니메이션이 끝나도 창을 열어두는 프로세스
plt.waitforbuttonpress()
