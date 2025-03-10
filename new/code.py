import requests
from bs4 import BeautifulSoup


def parser_boss(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('Error occurred, unable to fetch the page.')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('h1', class_='post-title')
    # If the title exists, return the text, otherwise return 'Title Not Found'
    if title_tag:
        return title_tag.get_text(strip=True)
    else:
        return 'Title Not Found'




# if movie_data:
#     print("Movie Title:")
#     print(movie_data)
# else:
#     print("Movie title could not be fetched.")
