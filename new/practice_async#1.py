import asyncio


async def parse_one():
    print('Parse one started.')
    await asyncio.sleep(2)
    print('Parse 1 ended.')

async def parser_two():
    print('Parse 2 started.')
    await asyncio.sleep(3)
    print('Parse 2 ended.')

async def main_f():
    await asyncio.gather(parse_one(), parser_two())

if __name__ == '__main__':
    asyncio.run(main_f())