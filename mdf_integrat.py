import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import os
from wordcloud import WordCloud
from stopwords import get_stopwords

import matplotlib.pyplot as plt


# Funció que recupera les imatges associades a cada entrada i les
# emmagatzema en una carpeta a part
def desa_img(artname, url_file):
    # Si és necessari, crear carpeta per a desar les imatges
    path = 'fotos_2'
    exists = os.path.exists(path)
    if not exists:
        os.mkdir(path)

    # Crear fitxer i escriure-hi el contingut de la imatge
    file_name = artname + '.jpg'
    # print(file_name)
    # Repòs de 2 segons per prevenció de bloqueig
    time.sleep(2)
    response = requests.get(url_file)
    file = open(path + '/{}'.format(file_name), "wb")
    file.write(response.content)
    file.close()


# Funció per a extreure el text complet d'un article
def extreu_text(url_article):
    # Cadena de caràcters amb el text a tornar
    art_text = ''

    # Repòs de 2 segons per prevenció de bloqueig
    time.sleep(2)

    page_art = requests.get(url_article)
    soup_pga = BeautifulSoup(page_art.content, 'html.parser')

    # Cada text a l'entrada va delimitada pels tags <article> i a dins es pot trobar tags <p>
    # que contenen el text. Però no tots els tags contenen text d'interès.
    soup_art = soup_pga.body.article

    for ptag in soup_art.find_all('p'):
        # Si el tag <p> conté atributs, com ara style o class, es pot descartar
        if not ptag.attrs:
            for chl in ptag.children:
                # Si el tag <p> no té cap fill, és un text normal, afegir-lo
                if chl.name is None:
                    art_text = art_text + chl.string + '\n'
                # Si té un fill i no és el tag <a> ni <br> cal afegir el text
                elif chl.name not in ['a', 'br']:
                    print(chl.string)
                    art_text = art_text + chl.string + '\n'

                # Al final del procés eliminar els salts de línia doble
                # que ha afegit en trobar un tag <br>
                art_text = art_text.replace('\n\n', '\n')

    return art_text


# Funció per a generar un núvol de tags per a un text donat
def nuvol_tags(text_conv):
    stop_words = get_stopwords('catalan')

    # Generate word cloud
    wordcloud = WordCloud(width=1500, height=1000, random_state=1,
                          background_color='#fff8e6', colormap='tab20b',
                          collocations=False, stopwords=stop_words).generate(text_conv)
    # Plot
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig('art_wordcloud.png')


url = "https://mercatflors.cat/blog/reflexions-entorn-dun-confinament/"
csv_file_name = 'mdf.csv'

# Pas 1. Navegació per una pàgina amb scroll infinit (Selenium)
profile = webdriver.FirefoxProfile()

# Canvi del user-agent a la petició per simular un navegador
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

# Pas 2. Lectura de l'estructura de la pàgina web completa
# Cada entrada va delimitada pels tags <article> i disposa de la url a l'article
soup_body = soup.body

# Inicialització de les variables a afegir al csv
ids = []
titols = []
dates = []
image = []
phrase = []
textos = []

# Per cada article publicat, extreure la informació d'interès i desar-la a csv
for i, article in enumerate(soup_body.find_all('article')):
    # Cerquem el tag <a> per recuperar enllaç a article i altra informació
    tag = article.find('a')

    # Obtenció del títol
    titols.append(tag.string)
    # Crida a la funció extreu_text per a obtenir l'article complet
    textos.append(extreu_text(tag['href']))
    # Obtenció de la data de publicació
    dates.append(article.find('time')['datetime'])
    # Obtenció de l'enllaç a la imatge associada
    image.append(article.find('img')['src'])
    # Obtenció de la frase resum de l'article, primer tag <p>
    tag2 = article.find('p')
    phrase.append(tag2.string)

    # Afegir identificador de l'entrada, num correlatiu de 1 a max
    ids.append(i+1)

    # Crida a la funció desa_img() per a guardar la imatge a la carpeta
    desa_img(tag.string, article.find('img')['src'])

    # Crida a la funció nuvol_tags per a un article per a generar imatge cloudtag
    if i == 2:
        nuvol_tags(extreu_text(tag['href']))

# Creació del diccionari base per a crear el dataframe
data = {'ID': ids, 'Títol': titols, 'Data': dates, 'Text': textos, 'ImageURL': image, 'Frase': phrase}
articles_frame = pd.DataFrame(data)

# Creació del fitxer csv a partir del dataframe
articles_frame.to_csv(csv_file_name, index=False)

"""
    with open(file_name, 'a') as f:
        f.write(str(i+1) + ',' + tag.string + ',' + article.find('time')['datetime'] +
                ',' + tag['href'] + ',' + '"Text, Article"' + ',' + tag2.string + '\n')
"""

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