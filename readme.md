**Drafts for web scraping project**

**xkcd.py**


El fitxer xkcd.py és un petit experiment que he escrit per començar
a practicar web scraping. El fitxer extreu el missatge flotant que apareix a la 
pàgina de xkcd.com quan deixem el cursor a sobre de la imatge. Funciona per a qualsevol 
de les pàgines de xkcd, només cal canviar la url 'https://xkcd.com', que ens porta 
a la imatge més recent, per una d'anterior, per exemple 'https://xkcd.com/2592/'

XKCD és un webcomic que fa molt de temps que segueixo, el trobo molt divertit. Té
un humor molt enginyós i surrealista, i el missatge flotant que sempre apareix a
cada imatge sempre és fins i tot més surrealista...

**xkcd2.py**

Aquest segon fitxer és una complexificació del primer, la diferència és
que aquest extreu diversos missatges flotants d'un rang de pàgines publicades 
consecutivament. Tècnicament, entra a diverses pàgines del mateix lloc web.
Des d'aquí, fàcilment (crec) es podria extreure altres elements de les mateixes
pàgines per crear un diccionari o dataframe. El dataset resultant podria
incloure, per exemple, títol del còmic, enllaç a la imatge del còmic,
missatge flotant... tot per un nombre de pàgines a definir, per exemple,
les últimes 30 pàgines publicades en relació a la data en que s'executa 
el fitxer.