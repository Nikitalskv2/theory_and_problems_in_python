import asyncio
import time

async def task1():
    await asyncio.sleep(1)
    print("Task 1 done")

    print(time.time())

async def task2():
    await asyncio.sleep(2)
    print("Task 2 done")

    print(time.time())

async def main():
    print(time.time())
    await task1()  # Ждём завершения task1
    await task2()  # Ждём завершения task2

