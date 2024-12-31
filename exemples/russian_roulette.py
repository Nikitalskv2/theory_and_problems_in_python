import asyncio
import random


async def trigger(position, p):
    await asyncio.sleep(position/2)
    if position == p:
        raise RuntimeError('Boom!')
    print('%d is ok' % (position+1))


async def roulette():
    p = random.randrange(0, 6)
    coros = (trigger(i, p) for i in range(6))
    try:
        await asyncio.gather(*coros)
    except RuntimeError as e:
        print(e)
    await asyncio.sleep(1)


asyncio.run(roulette())
