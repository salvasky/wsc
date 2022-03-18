from urllib.request import urlopen
from bs4 import BeautifulSoup

"""
Aquest segon fitxer és una complexificació del primer, la diferència és
que aquest extreu diversos missatges flotants d'un rang de pàgines publicades 
consecutivament. Tècnicament, entra a diverses pàgines del mateix lloc web.
Des d'aquí, fàcilment (crec) es podria extreure altres elements de les mateixes
pàgines per crear un diccionari o dataframe. El dataset resultant podria
incloure, per exemple, títol del còmic, enllaç a la imatge del còmic,
missatge flotant... tot per un nombre de pàgines a definir, per exemple,
les últimes 30 pàgines publicades en relació a la data en que s'executa 
el fitxer.
"""

lhtml =[]

for i in range(2587, 2593):
    lhtml.append(urlopen('https://xkcd.com/{}'.format(i)))

for w in lhtml:
    bs = BeautifulSoup(w, 'html.parser')

    line = []

    for child in bs.find(id='comic').children:
        line.append(str(child))

    t = line[1]

    start = 'title='
    end = '>'

    print((t.split(start))[1].split(end)[0])
