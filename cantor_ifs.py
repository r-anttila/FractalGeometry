import matplotlib.pyplot as plt
import numpy as np
import random

x = np.empty(0)
xk = 1


def F1(x): return 1/3*x


def F2(x): return 1/3*x+2/3


for _ in range(10000):
    var = random.randint(1, 10)

    if var <= 5:
        xk = F1(xk)
        x = np.append(x, xk)

    if var > 5:
        xk = F2(xk)
        x = np.append(x, xk)

plt.eventplot(x, orientation='horizontal', linelengths=0.2, linewidths=0.5)
plt.show()
