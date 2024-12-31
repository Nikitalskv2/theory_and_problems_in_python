'''
write/read через aiofiles исп. фсинхронные вызовы и обесп. неблокирующую работу

+ код не блокирует другие задачи при работе с файлом
+ полезно при высокой конкуренции, где работа с файлами одна из

- файловая система на уровне ОС остается синхронной, а асинхронность достигается за счет потоков через aiofiles
- выгода может быть меньше, чем ожидается
- ввозможна гонка данных, если несколько корутин одновременно пытаются работатть с одним файлом (исп. asyncio.Lock() )

'''
import asyncio
import aiofiles

lock = asyncio.Lock()


async def write_file(filename, context):
    async with lock:
        async with aiofiles.open(filename, mode='a') as f:
            await f.write(context)

asyncio.run(write_file("exemple.txt", "hello async world\n"))

