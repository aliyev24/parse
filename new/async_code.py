import aiohttp
from bs4 import BeautifulSoup

# Make the parser_boss function asynchronous
async def parser_boss(url):
    async with aiohttp.ClientSession() as session:  # Open an async session
        async with session.get(url) as response:    # Send the HTTP GET request asynchronously
            if response.status != 200:
                print('Error occurred, unable to fetch the page.')
                return None
            # Read the response text asynchronously
            html = await response.text()
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            title_tag = soup.find('h1', class_='post-title')
            
            # If the title exists, return the text, otherwise return 'Title Not Found'
            if title_tag:
                print(title_tag.get_text(strip=True))
            else:
                return 'Title Not Found'
        