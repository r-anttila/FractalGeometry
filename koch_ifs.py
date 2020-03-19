import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
import numpy as np
from math import *
import random


def F1(x, y): return [1/3*x, 1/3*y]


def F2(x, y): return [1/6*x-np.sqrt(3)/6*y+1/3, np.sqrt(3)/6*x+1/6*y]


def F3(x, y): return [1/6*x+np.sqrt(3)/6*y +
                      1/2, -np.sqrt(3)/6*x+1/6*y+np.sqrt(3)/6]


def F4(x, y): return [1/3*x+2/3, 1/3*y]


def random_iteration(num_points):
    x = np.empty(0)
    y = np.empty(0)

    xk = 0
    yk = 0

    for _ in range(num_points+1):
        var = random.randint(1, 12)

        if var > 0 and var <= 3:
            xk, yk = F1(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

        if var > 3 and var <= 6:
            xk, yk = F2(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

        if var > 6 and var <= 9:
            xk, yk = F3(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

        if var > 9:
            xk, yk = F4(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

    plt.figure(0)
    plt.scatter(x, y, s=0.01, marker=MarkerStyle(marker='*'))

    plt.axis('equal', xmin=-0.1, xmax=1.1, ymin=-0.2, ymax=1.2)


def recursive_iteration(rec_set, i, ax):
    f1xy = np.empty([0, 2])
    f2xy = np.empty([0, 2])
    f3xy = np.empty([0, 2])
    f4xy = np.empty([0, 2])

    if i == 0:
        plt.plot(rec_set[:, 0], rec_set[:, 1], c="blue")
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
    xy = np.array([[0, 0]])
    xy = np.append(xy, [[1, 0]], axis=0)
    recursive_iteration(xy, num_iters, plt.gca())
    plt.axis('equal')


if __name__ == "__main__":
    regular_iteration(6)
    random_iteration(10000)
    plt.show()
