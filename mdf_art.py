import requests
from bs4 import BeautifulSoup

# Import package for wordclouds
from wordcloud import WordCloud
from stopwords import get_stopwords

import matplotlib.pyplot as plt

# url = "https://mercatflors.cat/blog/sonia-gomez/"
url = "https://mercatflors.cat/blog/quim-bigas/"

art_text = ''

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Cada text a l'entrada va delimitada pels tags <article> i a dins es pot trobar tags <p>
# que contenen el text. Però no tots els tags contenen text d'interès.
soup_art = soup.body.article

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
            # que afegeix en trobar un tag <br>
            art_text = art_text.replace('\n\n', '\n')

# [PROVES] Escriptura del text a un fitxer per a veure el resultat final
with open('test_mdf.txt', 'w') as f:
    f.write(art_text)

# [PROVES] Generació d'un cloud tag amb el text extret
stop_words = get_stopwords('catalan')

# Generate word cloud
wordcloud = WordCloud(width=3000, height=2000, random_state=1,
                      background_color='#fff8e6', colormap='tab20b',
                      collocations=False, stopwords=stop_words).generate(art_text)
# Plot
# plot_cloud(wordcloud)
plt.figure(figsize=(40, 30))
plt.imshow(wordcloud)
plt.axis("off")
# plt.show()
plt.savefig('art_wordcloud.png')
