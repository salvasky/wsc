**Drafts for web scraping project**

El fitxer xkcd.py és un experiment que faig escriure per començar
a practicar web scraping. El fitxer extreu el missatge flotant que apareix a la 
pàgina de xkcd.com quan deixem el cursor a sobre de la imatge. Funciona per a qualsevol 
de les pàgines de xkcd, només cal canviar la url 'https://xkcd.com', que ens porta 
a la imatge més recent, per una d'anterior, per exemple 'https://xkcd.com/2592/'

XKCD és un webcomic que fa molt de temps que segueixo, el trobo molt divertit. Té
un humor molt enginyós i surrealista, i el missatge flotant que sempre apareix a
cada imatge sempre és fins i tot més surrealista...

Una possible complexificació del codi podria consistir a, per exemple, permetre una cerca
de missatges flotants entre dues dates diferents, obtenint un diccionari amb
dates i els continguts respectius dels missatges flotants, o fins i tot un 
dataframe amb més camps (missatge flotant + data + títol del còmic + link de la imatge del 
comic + ...)

