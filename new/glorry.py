import requests
from bs4 import BeautifulSoup


def parser_glorry(url):
    response = requests.get(url)
    page_content = response.text
    soup = BeautifulSoup(page_content, 'html.parser')

    list_items = soup.find_all('a')
    spisok = []

    for item in list_items:
        text = item.text.strip()
        if text:  # Only append non-empty text
            spisok.append(text)
    return spisok



