import requests
from bs4 import BeautifulSoup
import re
import os

r = requests.get(
    "https://zh.wikipedia.org/wiki/Template:2004%E5%B9%B4%E8%88%AA%E7%A9%BA%E4%BA%8B%E6%95%85"
)

temps = re.findall('<a href="(/wiki/Template:.*?)" title', r.text, re.S)
urls = []
for temp in temps:
    urls.append("https://zh.wikipedia.org/" + temp)
    #print(urls[-1])

for url in urls:
    print('rest:' + str(len(urls) - urls.index(url)))

    year = re.search('(\d\d\d\d)', url, re.S)
    if (year):
        newpath = 'my_python/' + year.group()
    if not os.path.isdir(newpath):
        os.makedirs(newpath)
    if (year):
        r1 = requests.get(url)
        sp = BeautifulSoup(r1.text, 'html.parser')
        block = sp.find(attrs={'class': "navbox-list navbox-odd plainlist"})
        next_urls = re.findall('a href="(/wiki/.*?)" title="', str(block),
                               re.S)
        for next_url in next_urls:
            r2 = requests.get("https://zh.wikipedia.org" + next_url)
            spp = BeautifulSoup(r2.text, 'html.parser')
            file_name = spp.find(attrs={'id': 'firstHeading'})
            if (file_name):
                print(file_name.string)
            body = spp.find(attrs={'id': 'mw-content-text'})
            if (body):
                with open('my_python/' + year.group() + '/' +
                          file_name.string + '.txt',
                          'w',
                          encoding='utf-8') as file:
                    file.write(body.text)

print('finish')
