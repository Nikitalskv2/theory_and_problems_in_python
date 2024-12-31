import time


timeout = time.perf_counter()


# from functools import lru_cache   # для кеширования уже вычисленных значений
# @lru_cache(maxsize=None)
def recurs_fibo(n):
    if n <= 1:
        return n
    else:
        return recurs_fibo(n-1) + recurs_fibo(n-2)


# print(recurs_fibo(35))
## 25 = 75025 -- 0.03
## 35 = 9227465 -- 3.23


def fors_fibo(n):
    mem = []
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(fors_fibo(145))   ## 145 = 898923707008479989274290850145 -- 0.000078s


print(f'{time.perf_counter() - timeout:.6f}')
