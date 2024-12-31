import asyncio


class Ticker:
    def __init__(self, delay, to):
        self.delay = delay
        self.i = 0
        self.to = to

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        if i >= self.to:
            raise StopAsyncIteration
        self.i += 1
        if i:
            await asyncio.sleep(self.delay)
        return i


async def main():
    # Создаем объект Ticker с задержкой 1 секунда и верхним пределом 5
    async for i in Ticker(delay=1, to=5):
        print(i)


asyncio.run(main())

