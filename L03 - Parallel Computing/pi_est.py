import random
import multiprocessing as mp
import time
import matplotlib.pyplot as plt


def in_circle(n):
    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)

    count = 0

    for i in range(n):
        origin_dist = rand_x**2 + rand_y**2

        if origin_dist <= 1:
            count += 1

    return count


def pi_est(I, p, L):
    pool = mp.Pool(processes=p)

    start = time.time()

    res = [pool.apply_async(in_circle, (L,)) for i in range(I)]

    pool.close()
    pool.join()

    chunk_count = [result.get() for result in res]

    pi_n = [4*chunk_inside*(1/L) for chunk_inside in chunk_count]
    pi_estimate = sum(pi_n)*(1/I)

    total_time = time.time() - start

    return [pi_estimate, total_time]


def plot_results(M_values, time_values):
    plt.figure()
    plt.plot(M_values, time_values)
    plt.xlabel("M")
    plt.ylabel("Execution time [s]")
    plt.show()

    speedup = [time_values[0]/i for i in time_values]

    plt.figure()
    plt.plot(M_values, speedup)
    plt.xlabel("M")
    plt.ylabel("Speedup")
    plt.show()


if __name__ == '__main__':
    L = 10000
    I = 1000
    P_max = mp.cpu_count()
    P = range(1, P_max+1)

    res = []

    for p in P:
        res.append(pi_est(I, p, L))

    times = [res[i][1] for i in range(P_max)]
    pis = [res[i][0] for i in range(P_max)]

    plot_results(P, times)
