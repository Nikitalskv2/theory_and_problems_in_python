from functools import wraps
import time


def slowlog(timer: float):
    def dec(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            if time.time()-start-timer >= 0.00001:
                print("sloooow")
            return res
        return inner
    return dec


@slowlog(3)
def my_func():
    time.sleep(2)
    print("done")

my_func()
