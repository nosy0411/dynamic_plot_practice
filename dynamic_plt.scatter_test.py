# 실시간 산란을 만들려면 x와y의 값을 업데이트하고 각 반복에서 산점을 추가하면됩니다.
# 이 경우 산점도는 일반적으로 평면의 별개의 점을 나타내며 점이 겹칠 가능성이 거의 없으므로
# 모든 그림을 지우지 않아도됩니다.

import numpy as np
import matplotlib.pyplot as plt
x = 0
for i in range(10000):
    x = x+0.04
    y = np.sin(x)
    plt.scatter(x, y, color="b")
    plt.title("Real Time plot")
    plt.xlabel("x")
    plt.ylabel("sinx")
    plt.pause(0.001)

plt.show()
