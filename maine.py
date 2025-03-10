import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urlunparse
import parser


# Replace this URL with the actual URL where your products are listed
base_url = "https://turbo.az/autos"
url = "https://turbo.az/"  # Put the target URL here

query_params = {
    "q[sort]": "",
    "q[make][]": 6,  # Audi (make ID 6)
    "q[model][]": "",  # Empty for model (or add a model if needed)
    "q[used]": "",
    "q[region][]": "",  # Add regions as needed
    "q[price_from]": 20000,
    "q[price_to]": "",  # Empty for price_to
    "q[currency]": "azn",
    "q[loan]": 0,
    "q[barter]": 0,
    "q[category][]": "",  # Add categories as needed
    "q[year_from]": "",
    "q[year_to]": "",
    "q[color][]": "",
    "q[fuel_type][]": "",
    "q[gear][]": "",
    "q[transmission][]": "",
    "q[engine_volume_from]": "",
    "q[engine_volume_to]": "",
    "q[power_from]": "",
    "q[power_to]": "",
    "q[mileage_from]": "",
    "q[mileage_to]": "",
    "q[only_shops]": "",
    "q[prior_owners_count][]": "",
    "q[seats_count][]": "",
    "q[market][]": "",
    "q[crashed]": 1,
    "q[painted]": 1,
    "q[for_spare_parts]": 0,
    "q[availability_status]": "",
    "page": 2,  # pagination
}

# Use urlencode to encode the parameters
encoded_query = urlencode(query_params, doseq=True)

full_url = f"{base_url}?{encoded_query}"

# Custom headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


parser.turbo_parser(full_url, headers=headers)
