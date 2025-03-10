import aiohttp
from bs4 import BeautifulSoup

async def parser_glorry(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status!=200:
                print('Error occured')
            
            html = await response.text()
            soup = BeautifulSoup(html,'html.parser')
            list_items = soup.find_all('a')
            spisok = []

            for item in list_items:
                text = item.text.strip()
                if text:  # Only append non-empty text
                    spisok.append(text)
            print(spisok)


