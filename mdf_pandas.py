import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import os

url = "https://mercatflors.cat/blog/reflexions-entorn-dun-confinament/"
file_name = 'mdf.csv'


# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')


# with open('test_mdf_confi.html', 'w') as f:
#     f.write(soup.prettify())

# Navegació a una pàgina amb scroll infinit
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override",
                       "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0")
driver = webdriver.Firefox()
driver.get(url)

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Cada entrada al blog va delimitada pels tags <article> i disposa de la seva url
# Recollir totes les URLs, accedir-hi una a una i extreure la informació d'interès
soup_body = soup.body

titols = []
links = []
dates = []
image = []
phrase = []
# text = []

# Creació del fitxer csv on s'emmagetzemaran les dades
with open(file_name, 'w') as f:
    f.write('"ID","Title","Date","URL(prov)","Text","Phrase"\n')

# Per cada article publicat, extreure informació d'interès i desar-la a csv
for i, article in enumerate(soup_body.find_all('article')):
    tag = article.find('a')
    titols.append(tag.string)
    links.append(tag['href'])
    dates.append(article.find('time')['datetime'])
    image.append(article.find('img')['src'])
    tag2 = article.find('p')
    phrase.append(tag2.string)


data = {'Title': titols, 'Dates': dates, 'URL': links, 'Image URL': image, 'Frase': phrase}

articles_frame = pd.DataFrame(data)


articles_frame.to_csv('articles_p.csv', index=False)

"""
    with open(file_name, 'a') as f:
        f.write(str(i+1) + ',' + tag.string + ',' + article.find('time')['datetime'] +
                ',' + tag['href'] + ',' + '"Text, Article"' + ',' + tag2.string + '\n')
"""
# Prova d'impressió de les dates, títols i frases dels posts
# print(dates)
# print(titols)
print(phrase)
"""
# Creació d'un fitxer que emmagatzema les fotos de les artistes en format jpg
noms = titols

path = 'fotos'
exists = os.path.exists('fotos')
if not exists:
    os.mkdir('fotos')

for i in image:
    file_name = str(noms[0]) + '.jpg'
    print(file_name)
    response = requests.get(i)
    file = open('fotos/{}'.format(file_name), "wb")
    file.write(response.content)
    file.close()
    noms.pop(0)
"""