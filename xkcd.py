from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://xkcd.com')
bs = BeautifulSoup(html, 'html.parser')

line = []

for child in bs.find(id='comic').children:
    line.append(str(child))

t = line[1]

start = 'title='
end = '>'

print((t.split(start))[1].split(end)[0])