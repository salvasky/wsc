import requests
from bs4 import BeautifulSoup

url = "https://mercatflors.cat/blog/sonia-gomez/"
# url = "https://mercatflors.cat/blog/quim-bigas/"

art_text = ''

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# st = BeautifulSoup('<b class="boldest" style="text-align:right">Extremely bold</b>')
# print(st.b.attrs.keys())

# Cada text a l'entrada va delimitada pels tags <article> i a dins es pot trobar tags <p>
# que contenen el text. Però no tots els tags contenen text d'interès.
soup_art = soup.body.article

for ptag in soup_art.find_all('p'):
    # Si el tag <p> conté atributs, com ara style o class, es pot descartar
    if not ptag.attrs:
        for chl in ptag.children:
            if chl.name is None:
                # print('I have no children')
                print(chl.string)
                art_text = art_text + chl.string + '\n'
            elif chl.name not in ['a']:
                if chl.name == 'br':
                    print('Salt BR')
                    # art_text = art_text + '\n'
                else:
                    print(chl.string)
                    art_text = art_text + chl.string

# [PROVES] Escriptura del text a un fitxer per a veure el resultat final
with open('test_mdf.txt', 'w') as f:
    f.write(art_text)
