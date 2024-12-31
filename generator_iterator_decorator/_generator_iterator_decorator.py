from functools import wraps
# используется для сохранения меты, docstring


def dec(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print("yo")
        result = func(*args, **kwargs)
        return result
    return wrap


@dec
def my_gen():
    a = 0
    b = 1
    for i in range(5):
        yield a
        a += b


# f = my_gen()
# a = list(f)     ## [0, 1, 2, 3, 4]
# b = list(f)     ## [] проходит только один раз
# print(a)
# print(b)

# 1
f = my_gen()
for _ in range(10):
    try:
        print(next(f))
    except StopIteration:
        print("stop")
        break

#2
for value in my_gen():
    print(value)
