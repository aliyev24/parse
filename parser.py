import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urlunparse

# Configure the logging module
logging.basicConfig(
    filename="scraper.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def turbo_parser(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        logging.error("The request timed out.")
        print("Request timed out.")
    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP request error: {e}")
        print(f"HTTP request error: {e}")

    else:
        # Check if the request was successful
        if response.status_code == 200:
            html_content = response.text

            soup = BeautifulSoup(html_content, "html.parser")

            tz_containers = soup.find(
                "div", class_="page-content page-content--grey"
            ).find_all("div", class_="tz-container")

            for container in tz_containers[4]:
                if container:
                    for product in container:
                        print(product.text.strip())

                else:
                    logging.warning("No products found with the specified class.")
                    print("No products found.")
        else:
            logging.error(
                f"Failed to retrieve the webpage. Status code: {response.status_code}"
            )
            print(f"Failed: {response.status_code}")
