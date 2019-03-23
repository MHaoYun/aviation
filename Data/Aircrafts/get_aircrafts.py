import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import json

headers={
        'Cookie' : '__cfduid=d23bc45cbc3424de3672911f3a7f3586d1552970353; __psuid=7da73ec48b6c6da78b9da10d17e5f486; _ga=GA1.3.1994008712.1552970356; _gid=GA1.3.665775409.1552970356; ps_rmt=y4zcitpiaw8iawaj%3A22q50mlzdtfjl2vc2x05hht0o32cxlx2; _pk_ses.1.9f6a=%2A; _pk_cvar.1.9f6a=false; ps_sessid=0NrwYn7XFSsCRdrTCcQzq9ssxE; _pk_id.1.9f6a=aa56f523abd4543d.1552970354.589.1553342433..; _gat=1',
        'Host' : 'www.planespotters.net',
        'User-Agent':'Chrome/53.0.2785.116'
    }

def get_urls():
    
    r=requests.get("https://www.planespotters.net/production-list/index",headers=headers,timeout=5)

    results=re.findall('<a href="(/production-list.*?)">',r.text,re.S)

    nexts=set()
    for result in results:
        result='https://www.planespotters.net'+result
        nexts.add(result)
    nexts.discard('https://www.planespotters.net/production-list/index')

    results=list(nexts)        

    print('rest:::'+str(len(results)))
    
    filename = 'urls.json'
    with open(filename,'w') as f_obj:
        json.dump(results,f_obj)
 


get_urls()

filename ='urls.json'
with open(filename) as g_obj:
    nexts=json.load(g_obj)

with open('plane_data.csv','a') as csvfile:
        fieldnames=['Aircraft Type','Manufactor','Register number','Airline','Delivered date','Status']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
for next in nexts:
    print(next)
    print('rest: '+str(len(nexts)))
    company=re.search('/production-list/(.*?)/.*',next,re.S)
    print(company.group(1))
    max_page=1
    i=1
    final_results=[]
    while i<=max_page+1:
        
        r=requests.get(next+'?p='+str(i),headers=headers,timeout=10)
        time.sleep(0.033)

        soup=BeautifulSoup(r.text,'html.parser')
        num_pages=soup.find(attrs={'class':'pages'})
        
    
        #print(r.text)
        if(num_pages):
            numbers=re.search('.*\n(.*?)\n(.*?)\n',num_pages.text,re.S)
            new_max=int(numbers.group(1))
            if((new_max>=max_page)):
                max_page=int(numbers.group(1))

        print(str(i)+'/'+str(max_page+1))
        temps=soup.find_all(attrs={'class':'dt-td font-sm dt-td-min150 dt-col-sortable'})
        
        
        p=0
        while(p<len(temps)):
            temp_item={}
            temp_item['Manufactor']=company.group(1).strip()
            temp_item['Aircraft Type']=temps[p].text.strip()
            temp_item['Register number']=temps[p+1].find_previous_sibling().text.strip()
            temp_item['Airline']=temps[p+1].text.strip()
            temp_item['Delivered date']=temps[p+1].find_next_sibling().text.strip()
            temp_item['Status']=temps[p+1].find_next_sibling().find_next_sibling().text.strip()
            final_results.append(temp_item)
            p=p+2
        
        
        i=i+1
        

    with open('plane_data_2.csv','a') as csvfile:
        fieldnames=['Aircraft Type','Manufactor','Register number','Airline','Delivered date','Status']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        for final_result in final_results:
            writer.writerow(final_result)

    print('ok!')
    nexts.remove(next)

    filename ='urls.json'
    with open(filename,'w') as g_obj:
        json.dump(nexts,g_obj)
    print('rest:::'+str(len(nexts)))