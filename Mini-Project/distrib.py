import numpy as np
import dask.array as da
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def mandelbrot(c, MAX_ITER=80):
    z = np.zeros(c.shape, dtype=type(c))
    div_time = np.zeros(z.shape, dtype=np.uint8)
    n = np.full(c.shape, True, dtype=bool)

    for i in range(MAX_ITER):
        z[n] = z[n]*z[n] + c[n]
        diverged = np.greater(np.abs(z), 2, out=np.full(
            c.shape, False), where=n)
        div_time[diverged] = i
        n[np.abs(z) > 2] = False
        if np.all((n == 0)):
            break
    return div_time


def plot_vectorized(WIDTH, HEIGHT, _chunks):
    start = timer()
    a = np.linspace(-2, 1, WIDTH).reshape((1, WIDTH))
    b = np.linspace(-1.5, 1.5, HEIGHT).reshape((HEIGHT, 1))
    c = a + 1j*b
    C = da.from_array(c, chunks=_chunks)
    n = C.map_blocks(mandelbrot, dtype=np.uint8).compute()
    end = timer()
    plt.figtext(0.5, 0.01, "Time to run: {:.2f} seconds".format(end-start), ha="center",
                fontsize=14, bbox={"facecolor": "white", "alpha": 0.5, "pad": 4})
    plt.imshow(n, cmap='magma')
    plt.show()


if __name__ == '__main__':
    plot_vectorized()
