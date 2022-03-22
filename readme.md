# **Possibles webs i datasets**

## **Paràmetres a avaluar per tal de fer la tria:**
(podem afegir paràmetres si cal...)

-La web ofereix una api (oficial)?

-Hi ha un document robots.txt?

-Requereix usuari i/o contrasenya?

-Hi ha restriccions de scraping?

-Ofereix la possibilitat d'incloure contingut audiovisual?

-Inspiració (punt 7 enunuciat)

-----

## xkcd.com

Crec que podem descartar xkcd, ja que la mateixa web ofereix una api amb tota
la informació que puc inaginar que podríem extreure.

-----

## Meteomuntanya

Web: http://meteomuntanya.cat/prediccio_muntanya/

Possible Dataset: Recull de dades presents a la pàgina: avisos destacats de seguretat (inclosa icona, títol
i text explicatiu), mapa de predicció general (emmagatzemar la imatge) i mapa d'avisos (emmagatzemar la imatge
i possiblement identificar els avisos activats)

-La web ofereix una api (oficial)?
Meteomuntanya obté les dades de meteo.cat, i aquesta té una rest api molt sofisticada, 
però en canvi la informació d'aquesta pàgina en concret
no sembla accessible a través de l'api. Sembla justificat doncs optar per l'scraping per 
aquesta pàgina i aquestes dades concretes.

-Hi ha un document robots.txt?
http://meteomuntanya.cat/robots.txt

-Requereix usuari i/o contrasenya?
No

-Hi ha restriccions de scraping? No explícites (però podem incloure request-delay)

-Ofereix la possibilitat d'incloure contingut audiovisual?
Sí, mapes i icones.

-Inspiració (punt 7 enunuciat)
Pel que veig, aquesta pàgina s'actualitza cada 3 dies aproximadament, i no hi ha cap enllaç a 
l'històric de prediccions. Per tant, un primer interès del projecte seria que
el dataset generat ofereix la possibilitat
de construir un magatzem històric de prediccions, és a dir, fer l'scraping seria 
una forma d'emmagatzemar (la informació bàsica de) les prediccions (en un format 
organitzat i condensat). 

D'altra banda, el dataset generat permetria 
presentar una versió més condensada de la informació present a la pàgina web (reduint-la als
avisos de seguretat i mapes, prescindint del text explicatiu). Si imaginem que tenim un negoci
a la muntanya (hostal, botiga de lloguer de material, guia d'activitats), aquesta informació
sintetitzada es podria adquirir de forma automàtica cada tres dies amb l'script que generem per
imprimir-ho, emmagatzemar-ho, incloure-ho a la pàgina web pròpia, newsletters, etc.


Comentaris:
No he fet cap prova de codi, però hauria de ser possible extreure la informació que ens interessa. 
Crec que els mapes i icones presenten un repte interessant.


-----

## Mercat de les flors

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
