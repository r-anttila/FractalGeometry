import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
import numpy as np
import random


def F1(x, y): return [1/2*x - 1/2*y, 1/2*x+1/2*y]


def F2(x, y): return [-1/2*x - 1/2*y+1, 1/2*x-1/2*y]


def random_iteration(num_points):
    x = np.empty(0)
    y = np.empty(0)

    xk = 0
    yk = 0

    for _ in range(num_points+1):
        var = random.randint(1, 10)

        if var <= 5:
            xk, yk = F1(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

        if var > 5:
            xk, yk = F2(xk, yk)
            x = np.append(x, xk)
            y = np.append(y, yk)

    plt.figure(0)
    plt.scatter(x, y, s=0.01, c='r', marker=MarkerStyle(marker='*'))

    plt.axis('equal')


def recursive_iteration(rec_set, i, ax):
    f1xy = np.empty([0, 2])
    f2xy = np.empty([0, 2])

    if i == 0:
        plt.plot(rec_set[:, 0], rec_set[:, 1], c="red")
    else:
        i -= 1
        for x, y in np.nditer([rec_set[:, 0], rec_set[:, 1]]):
            f1xy = np.append(f1xy, [F1(x, y)], axis=0)
            f2xy = np.append(f2xy, [F2(x, y)], axis=0)

        recursive_iteration(f1xy, i, ax)
        recursive_iteration(f2xy, i, ax)


def regular_iteration(num_iters):
    plt.figure(1)
    xy = np.array([[0, 0]])
    xy = np.append(xy, [[1, 0]], axis=0)
    recursive_iteration(xy, num_iters, plt.gca())


if __name__ == "__main__":
    # regular_iteration(13)
    random_iteration(100000)
    plt.gca().axis('equal')
    plt.show()
