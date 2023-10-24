from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, "lxml")

box = soup.find('article', class_='main-article')

links = []
for link in box.find_all('a', href=True):
  links.append(f"{root}/{link['href']}")

print(links)