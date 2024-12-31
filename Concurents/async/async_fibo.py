import asyncio
import time


async def cal_fib(n):
    if n <= 1:
        return n
    else:
        # Явно дожидаемся выполнения обеих ветвей
        fib1 = asyncio.create_task(cal_fib(n - 1))
        fib2 = asyncio.create_task(cal_fib(n - 2))
        return await fib1 + await fib2


async def period_mess():
    while True:
        print("message")
        await asyncio.sleep(0.5)


async def main():
    # asyncio.create_task(period_mess())
    # await period_mess()
    result = None
    start_time = time.time()
    result = await cal_fib(25)     ##   25 = 75025 -- 4.9s

    end_time = time.time()
    print(f"calculate 25 = {result} in {end_time - start_time:.2f}")

asyncio.run(main())
'''
Этот метод все еще неэффективен для больших n, 
так как вызывает экспоненциальное количество задач. 
Для оптимизации лучше использовать мемоизацию или итеративный подход.
'''