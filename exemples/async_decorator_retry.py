import asyncio
import random
from functools import wraps
from typing import Callable, List, Type


def dec(exception: List[Type[Exception]], delay: int, max_return: int):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_return):       # задаем количество попыток
                try:
                    return await func(*args, **kwargs)  # выполняем функцию
                except tuple(exception) as e:   # при неудаче
                    print(f"Attempt {attempt + 1} failed with {type(e).__name__}: {e}")
                    if attempt < max_return - 1:    # проверка на номер попытки
                        await asyncio.sleep(delay)
            raise RuntimeError(f"Function failed after {max_return} retries")
        return wrapper
    return decorator


@dec([IOError, TimeoutError], delay=1, max_return=5)
async def func():
    n = random.random()
    print(f'{n:.2f}')
    if n < 0.9:
        raise IOError("Simulated IO Error")
    return "Success!"


async def main():
    try:
        result = await func()
        print(result)
    except RuntimeError as e:
        print(e)


asyncio.run(main())