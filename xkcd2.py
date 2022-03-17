from urllib.request import urlopen
from bs4 import BeautifulSoup

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
