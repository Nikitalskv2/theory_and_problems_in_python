

# Пример 1: Асинхронность позволяет одновременно отправлять запросы к нескольким серверам, не ожидая ответа от каждого по очереди.

import asyncio
import httpx


async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f"Загружено: {url}, статус: {response.status_code}")
        return response.status_code


async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org",
        "https://jsonplaceholder.typicode.com/posts"
    ]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print("Все данные загружены!")

asyncio.run(main())

# Пример 2: Асинхронная обработка задач с тайм-аутами
# Асинхронность позволяет обрабатывать задачи с учетом их времени выполнения.

#import asyncio
#
# async def process_task(name, delay):
#     print(f"Начало выполнения задачи {name}")
#     await asyncio.sleep(delay)
#     print(f"Задача {name} завершена за {delay} секунд")
#
# async def main():
#     tasks = [
#         process_task("A", 2),
#         process_task("B", 1),
#         process_task("C", 3),
#     ]
#     await asyncio.gather(*tasks)
#     print("Все задачи выполнены!")
#
# asyncio.run(main())