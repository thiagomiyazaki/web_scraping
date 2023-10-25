from bs4 import BeautifulSoup
import sqlite3
import requests

connection = sqlite3.connect('transcripts.db')
connect_cursor = connection.cursor()
connect_cursor.execute("""CREATE TABLE transcripts(
                            title text,
                            transcript text
)""")
connection.commit()


root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, "lxml")

box = soup.find('article', class_='main-article')

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

connection = sqlite3.connect('transcripts.db')
connect_cursor = connection.cursor()

for link in links:
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, "lxml")

    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    connect_cursor.execute(f"INSERT INTO transcripts VALUES ('{title}','{title}')")

    connection.commit()

connection.close()

    
    