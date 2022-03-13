from cmath import inf
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
import multiprocessing as mp


def mandelbrot(c, MAX_ITER=80):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n


def parallel_loop(P, L, N):
    X = np.linspace(-2, 1, N)
    Y = np.linspace(-1.5, 1.5, N)
    C = [x+1j*y for x in X for y in Y]
    pool = mp.Pool(processes=P)
    n = pool.map(mandelbrot, iterable=C, chunksize=L)
    pool.close()
    pool.join()
    n = np.reshape(n, (N, N))
    n = np.transpose(n)

    return n


def plot_parallel():
    start = timer()
    n = parallel_loop(6, 1000, 1500)
    end = timer()
    plt.figtext(0.5, 0.01, "Time to run: {:.2f} seconds".format(end-start), ha="center",
                fontsize=14, bbox={"facecolor": "white", "alpha": 0.5, "pad": 4})
    plt.imshow(n, cmap='magma')
    plt.show()


def optimal_chunk():
    N = 1500
    L = [1, 10, 100, 1000, 1500]
    fastest_t = np.Infinity
    fastest_p = 0
    chunk_size = 0

    times = np.array([])
    for p in range(1, mp.cpu_count()+1):
        for c in L:
            start = timer()
            n = parallel_loop(p, c, N)
            end = timer()
            times = np.append(times, end-start)
            if end-start < fastest_t:
                fastest_t = end-start
                fastest_p = p
                chunk_size = c
    print("Fastest time: {}\n Number of processors: {}\n Chunk size: {}".format(
        fastest_t, fastest_p, chunk_size))


def compare():
    L = 1000
    N = 1500
    P = range(1, mp.cpu_count()+1)
    time_values = []
    for p in range(1, mp.cpu_count()+1):
        start = timer()
        n = parallel_loop(p, L, N)
        end = timer()
        time_values.append(end-start)
    plt.figure()
    plt.plot(P, time_values)
    plt.xlabel("M")
    plt.ylabel("Execution time [s]")
    plt.show()

    speedup = [time_values[0]/i for i in time_values]

    plt.figure()
    plt.plot(P, speedup)
    plt.xlabel("M")
    plt.ylabel("Speedup")
    plt.show()


if __name__ == '__main__':
    compare()
