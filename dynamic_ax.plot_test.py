import numpy as np
import time
import matplotlib.pyplot as plt

# plt.ion()은 대화식 모드를 켭니다. 플롯이 호출되지 않으면 플롯이 업데이트되지 않습니다.
plt.ion()
fig, ax = plt.subplots()


# 초기 축 범위 설정. 초기 축 범위 제한이 없다면 scatter는 자동으로 축을 업데이트 해나감
# 실시간으로 축이 조정된다면 딱히 효과는 없을 수 있음
ax.set_xlim(0, 100)
ax.set_ylim(-1, 1)
ax.grid(True)

# xlim이나 ylim으로 사전에 축에 대한 한계를 정하면 relim이나 autoclase_view()의 효과는 사라짐
# 따라서 실시간으로 축이 조정되게 하려면 bound는 제거하거나 relim 또는 autoscale_view()에 영향을 주면 안됨


# 범위를 설정해도 축 업데이트를 하는 법
# ax.axis('auto')
# set_autoscale_on은 자동으로 x,y축을 업데이트 해줌
ax.set_autoscale_on(True)
# y축만 업데이트 하고 싶으면 set_autoscaley_on(True)
# x축만 업데이트 하고 싶으면 set_autoscalex_on(True)

x = np.linspace(0, 10, 100)
y = np.cos(x)

# plot 테스트
# 초기 값이 들어가야 함. ax.plot([],[])는 그냥 빈 공간만 그리고 업데이트 안됨
line1, = ax.plot(x, y)

for p in range(100):
    update_x = np.linspace(0+p, 10+p, 100)
    update_y = np.cos(update_x-0.05*p)

    # plot 테스트
    line1.set_xdata(update_x)
    line1.set_ydata(update_y)
    # 또는 위와 같이 말고, lines, = set_data(x,y) 도 가능함

    # ax.relim()과 ax.autoscale_view()는 set_data후에 draw 전에 설정되야함. 그리고 이 2개는 세트로 있어야지 효과있음
    # Relim : Recompute the data limits based on current artists.
    ax.relim()
    ax.autoscale_view()
    # reason : The data limits are not updated automatically
    # when artist data are changed after the artist has been added to an Axes instance.
    # In that case, use matplotlib.axes.Axes.relim() prior to calling autoscale_view.

    fig.canvas.draw()

    # plot으로 그려지는 line1이 새로운 set_data를 통해서 계속 업데이트 되고 그려지므로 안지워도 됨
    # fig.canvas.flush_events()

    time.sleep(0.001)

# 애니메이션이 끝나도 창을 열어두는 프로세스
plt.waitforbuttonpress()
