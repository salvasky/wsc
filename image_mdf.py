import requests
from bs4 import BeautifulSoup

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
import os.path

url = "https://mercatflors.cat/blog"
url_2 = "https://mercatflors.cat/blog/reflexions-entorn-dun-confinament/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

page_2 = requests.get(url_2)
soup_2 = BeautifulSoup(page_2.content, 'html.parser')

# print(soup.prettify())
with open('test_mdf.html', 'w') as f:
    f.write(soup.prettify())

with open('test_mdf_confi.html', 'w') as f:
    f.write(soup_2.prettify())

# La inspecció dels HTML mostra que hi ha scroll infinit a les dues pàgines.
# Informació sobre scraping amb infinit scrolling with selenium:
# https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7
# https://github.com/LimonSafayet/Web-Scraping-in-Python

# Proves de navegació a una pàgina amb scroll infinit
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override",
                       "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0")
driver = webdriver.Firefox()
driver.get("https://mercatflors.cat/blog/reflexions-entorn-dun-confinament/")

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

soup_inf = BeautifulSoup(driver.page_source, 'html.parser')
# soup = BeautifulSoup(driver.page_source, 'lxml')
# html parser ha funcionat

# with open("test_inf.html", 'w') as f:
#     f.write(soup_inf.prettify())

# Cada entrada al blog va delimitada pels tags <article> i disposa de la seva url
# Recollir totes les URLs, accedir-hi una a una i extreure la informació d'interès
soup_body = soup_inf.body

titols = []
links = []
dates = []
image = []
text = []

for article in soup_body.find_all('article'):
    tag = article.find('a')
    titols.append(tag.string)
    links.append(tag['href'])
    dates.append(article.find('time')['datetime'])
    image.append(article.find('img')['src'])

# Prova d'impressió de les dates dels posts
print(titols)

noms = titols

os.mkdir('fotos')

for i in image:
    file_name = str(noms[0]) + '.jpg'
    print(file_name)
    response = requests.get(i)
    file = open('fotos/{}'.format(file_name), "wb")
    file.write(response.content)
    file.close()
    noms.pop(0)


