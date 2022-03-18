from urllib.request import urlopen
from bs4 import BeautifulSoup

"""
El fitxer xkcd.py és un petit experiment que he escrit per començar
a practicar web scraping. El fitxer extreu el missatge flotant que apareix a la 
pàgina de xkcd.com quan deixem el cursor a sobre de la imatge. Funciona per a qualsevol 
de les pàgines de xkcd, només cal canviar la url 'https://xkcd.com', que ens porta 
a la imatge més recent, per una d'anterior, per exemple 'https://xkcd.com/2592/'

XKCD és un webcomic que fa molt de temps que segueixo, el trobo molt divertit. Té
un humor molt enginyós i surrealista, i el missatge flotant que sempre apareix a
cada imatge sempre és fins i tot més surrealista...
"""

html = urlopen('https://xkcd.com')
bs = BeautifulSoup(html, 'html.parser')

line = []

for child in bs.find(id='comic').children:
    line.append(str(child))

t = line[1]

start = 'title='
end = '>'

print((t.split(start))[1].split(end)[0])