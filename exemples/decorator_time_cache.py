import time


def cache(expiry_time):
    def decorator(func):
        memory_cache = {}

        def wrapper(*args, **kwargs):
            key = (*args, *kwargs.items())
            if key in memory_cache:
                value, timestamp = memory_cache[key]
                if time.time() - timestamp < expiry_time:
                    print("Retrieving result from cache...")
                    return value
            result = func(*args, **kwargs)
            memory_cache[key] = (result, time.time())
            return result
        return wrapper
    return decorator


@cache(3)
def calculate_multiply(a, b):
    return a * b


print(calculate_multiply(2, 3))
time.sleep(4)
print(calculate_multiply(2, 5))



