from timeit import default_timer as timer

import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(start_x=-2, end_x=1, start_y=-1.5, end_y=1.5, WIDTH=1500, HEIGHT=1500, MAX_ITER=80):
    a = np.linspace(start_x, end_x, WIDTH)
    b = np.linspace(start_y, end_y, HEIGHT)
    n = np.zeros((WIDTH, HEIGHT))
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z = 0
            c = x + 1j*y
            while abs(z) <= 2 and n[j, i] < MAX_ITER:
                z = z*z + c
                n[j, i] += 1
    return n


def plot_naive():
    start = timer()
    n = mandelbrot()
    end = timer()
    plt.figtext(0.5, 0.01, "Time to run: {:.2f} seconds".format(end-start), ha="center",
                fontsize=14, bbox={"facecolor": "white", "alpha": 0.5, "pad": 4})
    plt.imshow(n, cmap='magma')
    plt.show()
