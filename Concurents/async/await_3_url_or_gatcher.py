import asyncio
import httpx
import time


timeout = time.perf_counter()


async def get_data(url):
    async with httpx.AsyncClient() as client:
        # httpx.AsyncClient не является потокобезопасным,
        # и его нельзя использовать одновременно в нескольких асинхронных задачах
        data1 = await client.get(url)
        data2 = await client.get(url)
        return print({data1, data2})
    ## 1.2s

##

# async def fetch(url):
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         return response
#
#
# async def get_data(url):
#     data = await asyncio.gather(
#         fetch(url),
#         fetch(url)
#     )
#     print(data)
    ## 1.6

asyncio.run(get_data(url="http://example.com"))
print(time.perf_counter() - timeout)


