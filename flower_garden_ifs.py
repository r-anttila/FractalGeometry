import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
import numpy as np
import random


def F1(x, y): return [1/3*x+1/3, 1/3*y+2/3]


def F2(x, y): return [-1/3*y+1/3, x]


def F3(x, y): return [1/3*y+2/3, -x+1]


def random_iteration(num_points):
    x = np.empty(0)
    y = np.empty(0)

    xk = 0
    yk = 0

    for _ in range(num_points+1):
        var = random.randint(1, 12)

        if var <= 2:
            xk, yk = F1(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

        if var > 2 and var <= 7:
            xk, yk = F2(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

        if var > 7:
            xk, yk = F3(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

    plt.figure(0)
    plt.scatter(x, y, s=0.01, marker=MarkerStyle(marker='*'))


def recursive_iteration(rec_set, i, ax):
    f1xy = np.empty([0, 2])
    f2xy = np.empty([0, 2])
    f3xy = np.empty([0, 2])

    if i == 0:
        ax.add_patch(plt.Polygon(rec_set))
    else:
        i -= 1
        for x, y in np.nditer([rec_set[:, 0], rec_set[:, 1]]):
            f1xy = np.append(f1xy, [F1(x, y)], axis=0)
            f2xy = np.append(f2xy, [F2(x, y)], axis=0)
            f3xy = np.append(f3xy, [F3(x, y)], axis=0)

        recursive_iteration(f1xy, i, ax)
        recursive_iteration(f2xy, i, ax)
        recursive_iteration(f3xy, i, ax)


def regular_iteration(num_iters):
    plt.figure(1)

    xy = np.array([[0, 0]])
    xy = np.append(xy, [[1, 0]], axis=0)
    xy = np.append(xy, [[1, 1]], axis=0)
    xy = np.append(xy, [[0, 1]], axis=0)

    recursive_iteration(xy, num_iters, plt.gca())


if __name__ == "__main__":
    regular_iteration(8)
    # random_iteration(20000)
    plt.show()
