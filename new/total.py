import asyncio
import async_glorry
import async_code


boss_url = 'https://boss.az/vacancies/247544' 
glorri="https://jobs.glorri.az/"

async def parse(*url):
    print('Start')
    await asyncio.gather(
        async_glorry.parser_glorry(url[1]),
        async_code.parser_boss(url[0])
        )
    print('End')

if __name__ == '__main__':
    asyncio.run(parse(boss_url, glorri))
