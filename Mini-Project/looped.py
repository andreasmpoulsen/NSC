from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(c, MAX_ITER=80):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n


def plot_naive():
    start = timer()
    a = np.linspace(-2, 1, 1500)
    b = np.linspace(-1.5, 1.5, 1500)
    n = np.zeros((1500, 1500))
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c = x + 1j*y
            n[j, i] = mandelbrot(c)
    end = timer()
    plt.figtext(0.5, 0.01, "Time to run: {:.2f} seconds".format(end-start), ha="center",
                fontsize=14, bbox={"facecolor": "white", "alpha": 0.5, "pad": 4})
    plt.imshow(n, cmap='magma')
    plt.show()


if __name__ == '__main__':
    plot_naive()
