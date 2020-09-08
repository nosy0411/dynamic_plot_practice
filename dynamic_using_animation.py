# 동적 그래프를 그리는 법은 크게 2가지가 있는데
# (1) plt.ion() 을 이용하는 방법
# (2) import matplotlib.animation as animation 즉 animation을 이용하는 방법

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = []
y = []

figure, ax = plt.subplots(figsize=(4, 3))
line, = ax.plot(x, y)
plt.axis([0, 4*np.pi, -1, 1])


def func_animate(i):
    x = np.linspace(0, 4*np.pi, 1000)
    y = np.sin(2 * (x - 0.1 * i))

    line.set_data(x, y)

    return line,


range(10)

ani = FuncAnimation(figure,
                    func_animate,
                    frames=10,
                    interval=50)

# ani.save(r'animation.gif', fps=10)

plt.show()


# ani = FuncAnimation(figure,
#                     func_animate,
#                     frames=10,
#                     interval=50)
# figure는 플롯이 업데이트 될 Figure 객체입니다.
# func_animate는 각 프레임에서 호출되는 함수입니다. 첫 번째 논거는 다음 값frames에서 나옵니다.
# frames = 10은range(10)과 같습니다. 0에서 9까지의 값은 각 프레임에서func_animate로 전달됩니다.
# 또한리스트 [0, 1, 3, 7, 12]와 같이 인터벌을 ‘프레임’에 할당 할 수도 있습니다.
# interval은 ms단위의 프레임 간 지연 시간입니다.

# fps 및dpi와 같은 매개 변수를 사용하여 애니메이션을gif 또는mp4에 저장할 수 있습니다.
