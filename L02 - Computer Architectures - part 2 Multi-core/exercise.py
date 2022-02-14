import random
import numpy as np
from timeit import default_timer as timer

# EXERCISE 2.1

def loop(a, b):
    i = 0
    s = 0
    while i < len(a):
        s += a[i]*b[i]
        i += 1
    return s

def loop_unrolled(a,b):
    i = 0
    sum1 = 0
    sum2 = 0
    while i < int(len(a)/2-1):
        sum1 += a[2*i] * b[2*i]
        sum2 += a[2*i+1] * b[2*i+1]
        i += 1
    return sum1+sum2

def loop_unrolled2(a,b):
    i = 1
    sum1 = 0
    sum2 = 0
    while i < N:
        sum1 += a[i - 1] * b[i - 1]
        sum2 += a[i] * b[i]
        i += 2
    return sum1+sum2

def loop_unrolled3(a,b):
    i = 1
    sum1 = 0
    sum2 = 0
    while i < N:
        temp1 = a[i - 1] * b[i - 1]
        temp2 = a[i] * b[i]
        sum1 += temp1
        sum2 += temp2
        i += 2
    return sum1+sum2

def loop_unrolled4(a,b):
    i = 1
    sum1 = 0
    sum2 = 0
    temp1 = 0
    temp2 = 0
    while i < N:
        sum1 += temp1
        temp1 = a[i - 1] * b[i - 1]
        sum2 += temp2
        temp2 = a[i] * b[i]
        i += 2
    return sum1+sum2

N = 2000000
a = [random.randint(0, N) for i in range(N)]
b = [random.randint(0, N) for i in range(N)]


start = timer()
loop(a,b)
end = timer()

print("loop: ", end-start)

start = timer()
loop_unrolled(a,b)
end = timer()

print("loop_unrolled: ", end-start)

start = timer()
loop_unrolled2(a,b)
end = timer()

print("loop_unrolled2: ", end-start)

start = timer()
loop_unrolled3(a,b)
end = timer()

print("loop_unrolled3: ", end-start)

start = timer()
loop_unrolled4(a,b)
end = timer()

print("loop_unrolled4: ", end-start)

# EXERCISE 2.2

def cache_blocking(a, size):
    i = 0
    NRUNS = 10
    while(i < NRUNS):
        j = 0
        while(j < size):
            a[j] = 2.3*a[j]+1.2
            j += 1
        i += 1

start = timer()
cache_blocking(a, 384000)
end = timer()

print("cache_blocking384: ", end-start)

start = timer()
cache_blocking(a, 768000)
end = timer()

print("cache_blocking768: ", end-start)

start = timer()
cache_blocking(a, 1536000)
end = timer()

print("cache_blocking1546: ", end-start)