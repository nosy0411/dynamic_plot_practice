# 작동 안됨. 그리고 어짜피 self.plt 로 pyplot은 동적으로 사용못해서 안쓰는게 낫다.
import numpy as np
import time
import matplotlib.pyplot as plt

# plt.ion()은 대화식 모드를 켭니다. 플롯이 호출되지 않으면 플롯이 업데이트되지 않습니다.
plt.ion()

x = np.linspace(0, 10, 100)
y = np.cos(x)

plt.plot(x, y)
plt.draw()
# plt.show()

for p in range(100):

    print(p)
    # plt.clf()       # 그래프를 초기화한다.

    update_x = np.linspace(0+p, 10+p, 100)
    update_y = np.cos(update_x-0.05*p)

    # plot 테스트
    plt.plot(update_x, update_y)
    plt.draw()

    time.sleep(0.001)
