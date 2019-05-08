import requests
from bs4 import BeautifulSoup
import re
import os

# words = [
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
#     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
# ]
# f = open("Data/Engine/web.txt", 'w')

# for word in words:
#     print("https://en.wikipedia.org/wiki/List_of_aircraft_engines#" + word)
#     r = requests.get(
#         "https://en.wikipedia.org/wiki/List_of_aircraft_engines#" + word)

#     f.write(r.text)

# f = open("Data/Engine/web.txt", 'r')
# text = f.read()

r = requests.get("https://en.wikipedia.org/wiki/List_of_aircraft_engines#A")
text = r.text
sp = BeautifulSoup(text, 'html.parser')
h3s = sp.find_all(name='h3')
num = 0
f2 = open("Data/Engine/engine_tri.txt", 'w')
for h3 in h3s:
    spans = h3.find_all(name='span')
    for span in spans:
        if span.string == '[':
            spans.remove(span)
    for span in spans:
        if span.string == ']':
            spans.remove(span)
    for span in spans:
        if span.string == 'Notes':
            spans.remove(span)
    for span in spans:
        if span.string == 'Variants':
            spans.remove(span)
    for span in spans:
        if span.string == 'More':
            spans.remove(span)

    for span in spans:
        if span.string:
            # print(str(spans.index(span)) + '===' + span.string)
            manufacture = span.string
    #print(manufacture)
    # if h3:
    #     ul = h3.next_sibling()
    #     lis = ul.find_all(name="li")
    #     for li in lis:
    #         print(li)
    if manufacture != "Zündapp":
        ul = h3.find_next(name="ul")
        #print(h3.find_next(name="ul"))
        lis = ul.find_all(name="li")
        for li in lis:
            if li.string:
                print("引擎制造商" + manufacture + ' ' + "制造 引擎" + li.string + '\n')
                num += 1
                f2.write("引擎制造商" + manufacture + ' ' + "制造 引擎" + li.string +
                         '\n')
print(num)
