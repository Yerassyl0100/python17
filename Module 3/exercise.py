import requests
from bs4 import BeautifulSoup


def parse_stopgame_catalog(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    games_blocks = soup.find_all('div', class_='tiles-item')

    for game_block in games_blocks:
        title = game_block.find('div', class_='title').text.strip()

        release_date = game_block.find('div', class_='tile-date').text.strip()

        print("Название:", title)
        print("Дата выхода:", release_date)
        print()


url = "https://stopgame.ru/games/catalog"

print(parse_stopgame_catalog(url))
