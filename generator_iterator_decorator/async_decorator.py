import asyncio


def async_decorator(func):
    async def wrapper(*args, **kwargs):
        print("Перед вызовом функции")
        result = await func(*args, **kwargs)  # Вызов асинхронной функции
        print("После вызова функции")
        return result
    return wrapper


@async_decorator
async def my_async_function(x, y):
    print(f"Выполняется асинхронная функция с аргументами {x} и {y}")
    await asyncio.sleep(1)  # Имитация асинхронной операции
    return x + y


async def main():
    result = await my_async_function(5, 3)
    print(f"Результат: {result}")

asyncio.run(main())
