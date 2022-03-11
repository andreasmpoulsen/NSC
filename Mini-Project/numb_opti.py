from numba import jit
import numba
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer


@jit
def mandelbrot_looped(start_x=-2, end_x=1, start_y=-1.5, end_y=1.5, WIDTH=1500, HEIGHT=1500, MAX_ITER=80):
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


@jit
def mandelbrot_vectorized(start_x=-2, end_x=1, start_y=-1.5, end_y=1.5, WIDTH=1500, HEIGHT=1500, MAX_ITER=80):
    a = np.linspace(start_x, end_x, WIDTH).reshape((1, WIDTH))
    b = np.linspace(start_y, end_y, HEIGHT).reshape((HEIGHT, 1))
    c = a + 1j*b
    z = np.zeros(c.shape, dtype=complex128)
    div_time = np.zeros(z.shape, dtype=int)
    n = np.full(c.shape, True, dtype=bool)

    for i in range(MAX_ITER):
        z[n] = z[n]*z[n] + c[n]
        diverged = np.greater(np.abs(z), 2, out=np.full(
            c.shape, False), where=n)  # Find diverging
        # set the value of the diverged iteration number
        div_time[diverged] = i
        n[np.abs(z) > 2] = False    # to remember which have diverged
    return div_time


def plot_vectorized_optimized():
    start = timer()
    n = mandelbrot_vectorized()
    end = timer()
    plt.figtext(0.5, 0.01, "Time to run: {:.2f} seconds".format(end-start), ha="center",
                fontsize=14, bbox={"facecolor": "white", "alpha": 0.5, "pad": 4})
    plt.imshow(n, cmap='magma')
    plt.show()


def plot_looped_optimized():
    start = timer()
    n = mandelbrot_looped()
    end = timer()
    plt.figtext(0.5, 0.01, "Time to run: {:.2f} seconds".format(end-start), ha="center",
                fontsize=14, bbox={"facecolor": "white", "alpha": 0.5, "pad": 4})
    plt.imshow(n, cmap='magma')
    plt.show()
