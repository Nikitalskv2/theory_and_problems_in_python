# декоратор фыполняет функцию N раз и выводит общее время работы

from functools import wraps
import time

def times(loop):
    def dec(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = time.monotonic()
            for _ in range(loop):
                res = func(*args, **kwargs)
            end = time.monotonic() - start_time
            print(f'функция {func.__name__} выполнена {loop} раз за {end} сек')
            return res
        return inner
    return dec

@times(5)
def func_t():
    time.sleep(0.2)

func_t()

# новый список id
# в томже порядке что recom_ids
# не содержит seen_ids

recom_ids = [2, 3, 1]
seen_ids = [3, 10, 20]
# filtered = [2, 1]

seen_set = set(seen_ids)
filtered = [r_id for r_id in recom_ids if r_id not in seen_set]
print(filtered)



# мода, вывести самые частые обьекты из списка
l = [3,4,0,9,6,7,9,0,8,6,7,3,9,6,7,9,8,5,7,2,0,5,7,3,0,4,3,9,8,6,7,6,3,5,8]


def mod(arr: list[int], count: int) -> int:
    dct = {}
    for i in range(len(arr)-1):
        if arr[i] in dct.keys():
            dct[arr[i]] += 1
        else:
            dct[arr[i]] = 1

    res = {}

    for i in range(count+1):
        key = 0
        val = 0
        for k, v in dct.items():
            if v > val:
                key = k
                val = v
        res[key] = val
        dct.pop(key)

    return res.keys()


# print(mod(l, 5))



# ступеньки 1 или 2

def steps(num: int) -> int:
    if num == 1:
        return 1
    n1 = 1
    n2 = 2

    for i in range(3, num + 1):
        n1, n2 = n2, n1 + n2
    return n2

print(steps(4))




