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


