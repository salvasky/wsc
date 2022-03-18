#**Possibles webs i datasets**

##**Paràmetres a avaluar per tal de fer la tria:**
(podem afegir paràmetres si cal...)

-La web ofereix una api (oficial)?

-Hi ha un document robots.txt?

-Requereix usuari i/o contrasenya?

-Hi ha restriccions de scraping?

-Ofereix la possibilitat d'incloure contingut audiovisual?

-----

##xkcd.com

Crec que podem descartar xkcd, ja que la mateixa web ofereix una api amb tota
la informació que puc inaginar que podríem extreure.

-----

##La Liga

Web: https://www.laliga.com/estadisticas

Possible Dataset: Dades actuals dels 10 màxims golejadors de la lliga, incloent
foto, imatge d'escut de l'equip, gols (per partit), etc.

-La web ofereix una api (oficial)?
No. N'hi ha un parell de no oficials, però que no generen el mateix
dataset que aquí proposo.

-Hi ha un document robots.txt?
Sí, força extens.

-Requereix usuari i/o contrasenya?
No

-Hi ha restriccions de scraping? Es demana un crawl-delay de 30s

-Ofereix la possibilitat d'incloure contingut audiovisual?
Sí, fotos dels jugadors, imatge d'escut de l'equip...

Comentaris:
Potser la temàtica és una mica avorrida, però les possibilitats de fer 
scraping les trobo bastant idònies (incloent imatges i solució
pel crawl-delay). Cada cap de setmana la llista canvia (si hi ha gols
en els partits), i això dóna un sentit dinàmic al projecte.
-----

##Mercat de les flors

Web: https://mercatflors.cat/blog

Dataset: llista d'articles escrits per un autor concret, incloent 
data de publicació, foto relacionada amb l'article, nom de l'artista relacionat
, etc.

-La web ofereix una api (oficial)?
No

-Hi ha un document robots.txt?
Sí, molt genèric, permet accés total.

-Requereix usuari i/o contrasenya?
No.

-Hi ha restriccions de scraping?
No ho sembla.

-Ofereix la possibilitat d'incloure contingut audiovisual?
Sí, fotos dels espectacles lligats a cada article.

Comentaris:
Sóc molt proper a la temàtica, m'interessa el material, i potser 
ens podem inspirar en el codi que ja has escrit en relació al wordpress(?).
No sé si ofereix tantes possibilitats de generar un dataset adient comparat amb 
La Liga... Es poden mirar altres opcions en blogs similars...

-----
