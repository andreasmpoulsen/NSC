# -*- coding: utf-8 -*-
import time
import multiprocessing as mp
import matplotlib.pyplot as plt
import numpy as np


def in_circle(n):
    coords = np.random.rand(n, 2)
    count = 0
    for i in range(n):
        if (coords[i][0])**2 + (coords[i][1])**2 < 1:
            count += 1
    return count


def parallel_pi(P, L, N):
    np.random.seed(42)
    pool = mp.Pool(processes=P)

    start = time.time()

    results = [pool.apply_async(in_circle, (L,)) for i in range(N)]

    pool.close()
    pool.join()

    K_values = [result.get() for result in results]

    pi_n = [4*K_value*(1/L) for K_value in K_values]
    pi_estimate = sum(pi_n)*(1/N)

    stop = time.time()
    time_ex = stop-start

    return [pi_estimate, time_ex]


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
    P_max = 6
    result_values = []
    L = 10
    P = range(1, P_max+1)
    for i in range(1, 7):
        print("L = {}".format(pow(10, i)))
        L = pow(10, i)
        N = round(10000000/L)
        result_values.append(parallel_pi(12, L, N))

    time_values = [result_values[i][1] for i in range(P_max)]
    pi_values = [result_values[i][0] for i in range(P_max)]
    pi_errors = [abs(pi_est-np.pi) for pi_est in pi_values]
    print(time_values)
    plot_results(P, time_values)
    print(pi_values)
    print(pi_errors)
