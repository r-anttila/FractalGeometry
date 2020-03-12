import matplotlib.pyplot as plt
import numpy as np
import random

x = np.empty(0)
y = np.empty(0)

xk = 0
yk = 0


def F1(x, y): return [1/2*x, 1/2*y]


def F2(x, y): return [1/2*x+1/4, 1/2*y+1/2]


def F3(x, y): return [1/2*x+1/2, 1/2*y]


for _ in range(10000):
    var = random.randint(1, 12)

    if var <= 4:
        xk, yk = F1(xk, yk)
        x = np.append(x, xk)
        y = np.append(y, yk)

    if var > 4 and var <= 8:
        xk, yk = F2(xk, yk)
        x = np.append(x, xk)
        y = np.append(y, yk)

    if var > 8:
        xk, yk = F3(xk, yk)
        x = np.append(x, xk)
        y = np.append(y, yk)


plt.scatter(x, y, s=0.2)
plt.show()
