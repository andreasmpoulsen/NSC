import random
from functools import reduce
import multiprocessing as mp


def gen_sums(N):
    integers = [random.randint(1, 100000) for i in range(N)]

    mapped = list(map(lambda i: 2**i-i**7, integers))
    odd = list(filter(lambda i: i % 2, mapped))
    sum = reduce((lambda i, j: i + j), odd)

    return sum


if __name__ == '__main__':
    P = 4
    N = 1000
    L = 1000

    pool = mp.Pool(processes=P)
    results = [pool.apply_async(gen_sums, (L,)) for i in range(N)]
    pool.close()
    pool.join()
    K_values = [result.get() for result in results]

    sum = reduce((lambda i, j: i + j), K_values)

    print(sum)
