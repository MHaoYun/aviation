import requests
import re
from bs4 import BeautifulSoup

types = []
for line in open('../AirlineDisaster/disaster.txt', 'r', encoding='utf-8'):
    p = re.compile(r'Type:(.*?) FlightNumber', re.S)
    type = re.findall(p, line)[0]
    if not type in types:
        types.append(type)
# print(len(types))
# print(types)

infos = ['Role', 'National origin', 'Manufacturer', 'First flight', 'Introduction', 'Status',
        'Primary users', 'Produced', 'Number built', 'Unit cost', 'Developed from']
headers = {
    'Host': 'en.wikipedia.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/66.0'
}

for type in types:
    url = 'https://en.wikipedia.org/wiki/' + type
    try:
        request = requests.get(url)
        if request.status_code == 200:
            file = open('aircraft_type.txt', 'a+', encoding='utf-8')
            text = request.text
            html_bs = BeautifulSoup(text, 'html.parser')
            contents = html_bs.select('.infobox tr')
            print(type)
            file.write(type + '\n')
            j = 0
            if len(contents) > 3:
                for i in range(3, len(contents)):
                    while j < 11:
                        if (contents[i].find(infos[j]) != -1):
                            tmp_str = contents[i].text.replace(infos[j], '').strip().replace('\n', ' ')
                            file.write(infos[j] + ': ' + tmp_str + '\n')
                            j += 1
                            break
                        else:
                            j += 1
                file.write('\n')
            file.close()
            print('success')
        else:
            print('not find')
    except:
        print('error')

