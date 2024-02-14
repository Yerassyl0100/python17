import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(markup=response.text,
                     features='html.parser'
                     )


quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
for i in range(len(quotes)):
    print(f"{i + 1})")
    print(quotes[i].text)
    print('=====================================')
    print(authors[i].text)
