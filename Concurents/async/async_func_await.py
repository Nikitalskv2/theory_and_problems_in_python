import asyncio
import time


t = time.perf_counter()


async def func(name, wait):
    await asyncio.sleep(wait)
    print(name)


async def main():
    task = [func("1", 1),
            func("2", 2),
            func("3", 3)
            ]
    await asyncio.gather(*task)

asyncio.run(main())
print(time.perf_counter() - t)
## 3s