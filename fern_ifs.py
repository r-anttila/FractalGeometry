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


def recursive_iteration(rec_set, i, ax):
    f1xy = np.empty([0, 2])
    f2xy = np.empty([0, 2])
    f3xy = np.empty([0, 2])
    f4xy = np.empty([0, 2])

    if i == 0:
        ax.add_patch(plt.Polygon(rec_set))
    else:
        i -= 1
        for x, y in np.nditer([rec_set[:, 0], rec_set[:, 1]]):
            f1xy = np.append(f1xy, [F1(x, y)], axis=0)
            f2xy = np.append(f2xy, [F2(x, y)], axis=0)
            f3xy = np.append(f3xy, [F3(x, y)], axis=0)
            f4xy = np.append(f4xy, [F4(x, y)], axis=0)

        recursive_iteration(f1xy, i, ax)
        recursive_iteration(f2xy, i, ax)
        recursive_iteration(f3xy, i, ax)
        recursive_iteration(f4xy, i, ax)


def regular_iteration(num_iters):
    plt.figure(1)

    xy = np.array([[1, 0]])
    xy = np.append(xy, [[1, 1]], axis=0)
    xy = np.append(xy, [[0.5, 1]], axis=0)
    recursive_iteration(xy, num_iters, plt.gca())


if __name__ == "__main__":
    # regular_iteration(8)
    random_iteration(100000)
    plt.axis('equal')
    plt.show()
