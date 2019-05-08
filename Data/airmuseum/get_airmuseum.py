import requests
from bs4 import BeautifulSoup
import re
import os

# r = requests.get("https://en.wikipedia.org/wiki/List_of_aerospace_museums")
# f = open("Data/airmuseum/web.txt", 'w')
# f.write(r.text)

f = open("Data/airmuseum/web.txt", 'r')
text = f.read()
f1 = open("Data/airmuseum/museum_tri", "w")
temps = re.findall('<li>(.*?)</li>', text, re.S)
num = 0
tri = []
for temp in temps:
    t = re.findall(
        '<a href=".*?" title=".*?">(.*?)</a>, <a href=".*?" title=".*?">(.*?)</a>',
        temp, re.S)
    if t:
        print("Name: " + t[0][0])
        print("Location: " + t[0][1])
        tri.append('博物馆' + t[0][0] + ' ' + '位置 ' + t[0][1] + '\n')
        num += 1
for item in tri:
    f1.writelines(item)
print(num)
