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


def plot_naive(_dtype):
    start = timer()
    a = np.linspace(-2, 1, 1500, dtype=_dtype)
    b = np.linspace(-1.5, 1.5, 1500, dtype=_dtype)
    n = np.zeros((1500, 1500), dtype=_dtype)
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
        plot_naive(np.float16)
    elif _dtype_ == "32":
        plot_naive(np.float32)
    elif _dtype_ == "64":
        plot_naive(np.float64)
    elif _dtype_ == "128":
        plot_naive(np.longdouble)
    else:
        print("{} is not a valid float size".format(_dtype_))
