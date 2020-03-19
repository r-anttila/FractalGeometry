import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
import numpy as np
import random


def F1(x, y): return [0, 0.16*y]


def F2(x, y): return [0.85*x+0.04*y, -0.04*x+0.85*y+1.6]


def F3(x, y): return [0.2*x-0.26*y, 0.23*x+0.22*y+1.6]


def F4(x, y): return [-0.15*x+0.28*y, 0.26*x+0.24*y+0.44]


def random_iteration(num_iters):
    x = np.empty(0)
    y = np.empty(0)

    xk = 0
    yk = 0

    for _ in range(num_iters+1):
        var = random.randint(1, 100)

        if var == 1:
            xk, yk = F1(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

        if var > 1 and var <= 86:
            xk, yk = F2(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

        if var > 86 and var <= 92:
            xk, yk = F3(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

        if var > 92:
            xk, yk = F4(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

    plt.scatter(x, y, s=0.01, c='green', marker=MarkerStyle(marker='*'))

    plt.axis('equal', xmin=-0.1, xmax=1.1, ymin=-0.2, ymax=1.2)
    plt.show()


if __name__ == "__main__":
    random_iteration(100000)
