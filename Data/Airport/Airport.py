import re
import requests
from requests_html import BaseSession

airport_html_url_provider = (f"http://airport.anseo.cn/c-china__page-{i}" for i in range(1, 10))
airport_html_content_provider = (requests.get(url).content.decode() for url in airport_html_url_provider)
airport_html_transformer = re.compile(r'<tr>[\w\W]+?_blank">([\w\W]+?)</a>[\w\W]+?href="(.+?)" title="(.+?)"[\w\W]+?span title="IATA CODE:(.*?)"[\w\W]+?span title="ICAO CODE:(.*?)"')
airport_name_impurities = re.compile(r'\s*|<br />')
airport_name_purifier = lambda x: airport_name_impurities.sub('', x.strip())
airport_html_content_transformed = (airport_html_transformer.findall(content) for content in airport_html_content_provider)
airport_html_content_flattened = (i for lst in airport_html_content_transformed for i in lst)
airport_name_purified = ((airport_name_purifier(impure), *tail) for impure, *tail in airport_html_content_flattened)

# for data in airport_name_purified:
#     print(data)

# airport_name_purified[0] = ('大理Xiaguan', 'http://airport.anseo.cn/detail/DX35023', '大理机场(Dali)', 'DLU', 'ZPDL')

sess = BaseSession()
airport_detail_content_transformer = lambda u: sess.get(u)
airport_parameters_transformer = lambda c: (i.text for i in c.html.xpath('/html/body/div[2]/div/div[2]/div/div[1]/div/div[3]/div/div[1]/ul/li'))
airport_detail_transformer = lambda c: airport_parameters_transformer(c)

airport_merged = ((name, *tail, *airport_detail_transformer(airport_detail_content_transformer(url))) for name, url, *tail in airport_name_purified)

for i in airport_merged:
    print(i)
