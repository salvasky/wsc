import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time

url = "https://mercatflors.cat/blog/reflexions-entorn-dun-confinament/"

# La inspecció dels HTML mostra que hi ha scroll infinit a les dues pàgines.
# Informació sobre scraping amb infinit scrolling with selenium:
# https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7
# https://github.com/LimonSafayet/Web-Scraping-in-Python

# Informació sobre canvi de user-agent de Firefox amb Selenium
# https://stackoverflow.com/questions/29916054/change-user-agent-for-selenium-web-driver

# Navegació amb scroll infinit usant Selenium
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override",
                       "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0")
driver = webdriver.Firefox(profile)
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

# titols = []
# links = []
# dates = []

with open("test.csv", 'w') as f:
    f.write('"ID","Title","Date","URL"\n')

# Per cada article publicat, extreure informació d'interès i desar-la a csv
for i, article in enumerate(soup_body.find_all('article')):
    tag = article.find('a')
    # titols.append(tag.string)
    # links.append(tag['href'])
    # dates.append(article.find('time')['datetime'])

    with open("test.csv", 'a') as f:
        f.write(str(i+1) + ',' + tag.string + ',' + article.find('time')['datetime'] + ',' + tag['href'] + '\n')

# Exemple de línia de csv (versió 1):
# "ID","Data","Títol","URL"
