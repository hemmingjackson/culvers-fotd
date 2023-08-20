import requests, os, sys
from bs4 import BeautifulSoup

url_template = 'https://www.culvers.com/restaurants/{}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def get_fotd(city):
    url = url_template.format(city)
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: Unable to retrieve data for {city}. Status code: {response.status_code}")
        sys.exit(1)

    if response.url == 'https://www.culvers.com/flavor-of-the-day':
        print(f"Invalid store entered. Try searching at https://www.culvers.com/flavor-of-the-day")
        sys.exit(1)

    soup = BeautifulSoup(response.content, 'html.parser')
    fotd = soup.strong.string
    print(f'Today\'s flavor of the day at {city} is {fotd}!')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fotd.py <city>")
        sys.exit(1)

    city = sys.argv[1]
    get_fotd(city)