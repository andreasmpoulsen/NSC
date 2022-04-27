"""Naive implementation of the mandelbrot algorithm

    This script calculates and plots the mandelbrot set given a numerical precision and a set resolution.
"""

from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(c: complex, MAX_ITER: int = 80) -> int:
    """
        Calculates the amount of iterations for a given complex number under the mandelbrot rules.

        ### Parameters
        c: complex
            Complex number to iterate over.
        MAX_ITER: int
            Maximum number of iterations.

        ### Returns
        n: int
            The number of iterations at divergence.
    """

    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n


def plot_naive(_dtype, height: int, width: int) -> None:
    """
        Plots the mandelbrot set with a specific numerical precision and resolution

        ### Parameters
        _dtype: datatype
            The type of the complex coordinates used in the mandelbrot calculations
        height: int
            Height component of the resolution. Determines the number of rows in the 2D mandelbrot set
        width: int
            Width component of the resolution. Determines the number of columns in the 2D mandelbrot set

        ### Returns
        None
    """
    start = timer()

    a = np.linspace(-2, 1, height, dtype=_dtype)
    b = np.linspace(-1.5, 1.5, width, dtype=_dtype)
    n = np.zeros((height, width), dtype=_dtype)
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
    _dtype_ = input("Please write a float size [16, 32, 64, 128]: ").strip()
    if _dtype_ == "16":
        plot_naive(np.float16, 1500, 1500)
    elif _dtype_ == "32":
        plot_naive(np.float32, 1500, 1500)
    elif _dtype_ == "64":
        plot_naive(np.float64, 1500, 1500)
    elif _dtype_ == "128":
        plot_naive(np.longdouble, 1500, 1500)
    else:
        print("{} is not a valid float size".format(_dtype_))
