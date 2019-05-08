from bs4 import BeautifulSoup
import requests

aircraft1 = ["717", "737", "747", "757", "767", "777", "787"]
aircraft2 = ["A220", "A300", "A310", "A320", "A330", "A340", "A350", "A380"]
aircraft3 = ["CRJ", "ERJ145", "ERJ-170系列", "EMB-110", "EMB-120客机", "EMB-121"]

for aircraft in aircraft1:
    print(aircraft)
    url = 'https://baike.baidu.com/item/波音' + aircraft
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36', }
    # requests_object = requests.get(url, headers=header, verify=False)
    requests_object = requests.get(url, headers=header)
    requests_object.encoding = 'utf-8'
    html = requests_object.text
    html_bs = BeautifulSoup(html, 'html.parser')
    content_list = html_bs.select('.para')
    filename = 'B' + aircraft + '.txt'
    file = open(filename, 'w', encoding='utf-8')
    for content in content_list:
        print(content)
        text = content.get_text().strip()
        file.write(text+'\n\n')
    file.close()

for aircraft in aircraft2:
    print(aircraft)
    url = 'https://baike.baidu.com/item/空中客车' + aircraft
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36', }
    # requests_object = requests.get(url, headers=header, verify=False)
    requests_object = requests.get(url, headers=header)
    requests_object.encoding = 'utf-8'
    html = requests_object.text
    html_bs = BeautifulSoup(html, 'html.parser')
    content_list = html_bs.select('.para')
    filename = aircraft + '.txt'
    file = open(filename, 'w', encoding='utf-8')
    for content in content_list:
        print(content)
        text = content.get_text().strip()
        file.write(text+'\n\n')
    file.close()

for aircraft in aircraft3:
    print(aircraft)
    url = 'https://baike.baidu.com/item/' + aircraft
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36', }
    # requests_object = requests.get(url, headers=header, verify=False)
    requests_object = requests.get(url, headers=header)
    requests_object.encoding = 'utf-8'
    html = requests_object.text
    html_bs = BeautifulSoup(html, 'html.parser')
    content_list = html_bs.select('.para')
    filename = aircraft + '.txt'
    file = open(filename, 'w', encoding='utf-8')
    for content in content_list:
        print(content)
        text = content.get_text().strip()
        file.write(text+'\n\n')
    file.close()



