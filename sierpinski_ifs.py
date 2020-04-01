import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
import numpy as np
import random


def F1(x, y): return [1/2*x, 1/2*y]


def F2(x, y): return [1/2*x+1/4, 1/2*y+1/2]


def F3(x, y): return [1/2*x+1/2, 1/2*y]


def random_iteration(num_points):
    x = np.empty(0)
    y = np.empty(0)

    xk = 0
    yk = 0

    for _ in range(num_points+1):
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

    plt.figure(0)
    plt.scatter(x, y, s=0.005, marker=MarkerStyle(marker='*'))


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


'''
def recursive_iteration(rec_set, i, ax):
    if i == 0:
        ax.add_patch(plt.Polygon(rec_set))
    else:
        i -= 1
        for func in [F1, F2, F3]:
            fxy = np.empty([0, 2])
            for x, y in np.nditer([rec_set[:, 0], rec_set[:, 1]]):
                fxy = np.append(fxy, [func(x, y)], axis=0)

            recursive_iteration(fxy, i, ax)
'''


def regular_iteration(num_iters):
    plt.figure(1)

    xy = np.array([[0, 0]])
    xy = np.append(xy, [[1, 0]], axis=0)
    xy = np.append(xy, [[0.5, 1]], axis=0)
    recursive_iteration(xy, num_iters, plt.gca())


def square_regular_iteration(num_iters):
    plt.figure(1)

    xy = np.array([[0, 0]])
    xy = np.append(xy, [[0, 1]], axis=0)
    xy = np.append(xy, [[1, 1]], axis=0)
    xy = np.append(xy, [[1, 0]], axis=0)
    recursive_iteration(xy, num_iters, plt.gca())


if __name__ == "__main__":
    # regular_iteration(7)
    random_iteration(100000)
    # square_regular_iteration(1)
    plt.gca().axis('equal')
    plt.show()
