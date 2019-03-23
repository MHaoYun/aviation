import requests
from bs4 import BeautifulSoup
import time
import csv
import json

headers={
        'Cookie' : '__cfduid=d23bc45cbc3424de3672911f3a7f3586d1552970353; __psuid=7da73ec48b6c6da78b9da10d17e5f486; _ga=GA1.3.1994008712.1552970356; _gid=GA1.3.665775409.1552970356; _pk_ses.1.9f6a=%2A; _pk_cvar.1.9f6a=false; ps_rmt=zjlq1dmscigm5dwf%3Aq2k0w95w0xgown7ttqpszotvp497rmyv; ps_sessid=TF8KDoya%2C8skBOPPvwZcPXMT%2CD; _pk_id.1.9f6a=aa56f523abd4543d.1552970354.419.1553171017..',
        'Host' : 'www.planespotters.net',
        'User-Agent':'Chrome/53.0.2785.116'
}

capitals=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num_pages={
    'A':9,'B':2,'C':3,'D':1,'E':2,'F':2,'G':2,'H':1,'I':2,'J':1,'K':1,'L':2,'M':2,'N':2,'O':1,'P':2,'Q':1,'R':2,'S':4,'T':3,'U':1,'V':1,'W':1,'X':1,'Y':1,'Z':1
}
for capital in capitals:
    current_url='https://www.planespotters.net/airlines/'+capital
    max_page=num_pages[capital]
    i=1
    while i<=max_page:
        r=requests.get(current_url+'/'+str(i),headers=headers,timeout=10)
        print(current_url+'/'+str(i))
        time.sleep(0.033)

        soup=BeautifulSoup(r.text,'html.parser')

        odd_nodes=soup.find_all(attrs={'class':'dt-odd'})
        even_nodes=soup.find_all(attrs={'class':'dt-even'})
        with open('airline_data.csv','a') as csvfile:
                fieldnames=['Airline_name','ICAO','IATA','Callsign','Country','Website']
                writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
                writer.writeheader()

        for odd_node in odd_nodes:
            temp_item={}
            Airline_name=odd_node.find(attrs={'class':'dt-first'})
            temp_item['Airline_name']=Airline_name.text.strip()
            temp_item['ICAO']=Airline_name.find_next_sibling().text.strip()
            temp_item['IATA']=Airline_name.find_next_sibling().find_next_sibling().text.strip()
            temp_item['Callsign']=Airline_name.find_next_sibling().find_next_sibling().find_next_sibling().text.strip()
            temp_item['Country']=Airline_name.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text.strip()
            Web=odd_node.find(attrs={'class':'dt-last'})
            Website=Web.find(name='a')
            if(Website):
                temp_item['Website']=Website.attrs['href']
            with open('airline_data.csv','a') as csvfile:
                fieldnames=['Airline_name','ICAO','IATA','Callsign','Country','Website']
                writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
                writer.writerow(temp_item)

        for even_node in even_nodes:
            temp_item={}
            Airline_name=even_node.find(attrs={'class':'dt-first'})
            temp_item['Airline_name']=Airline_name.text.strip()
            temp_item['ICAO']=Airline_name.find_next_sibling().text.strip()
            temp_item['IATA']=Airline_name.find_next_sibling().find_next_sibling().text.strip()
            temp_item['Callsign']=Airline_name.find_next_sibling().find_next_sibling().find_next_sibling().text.strip()
            temp_item['Country']=Airline_name.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text.strip()
            Web=even_node.find(attrs={'class':'dt-last'})
            Website=Web.find(name='a')
            if(Website):
                temp_item['Website']=Website.attrs['href'] 
            with open('airline_data.csv','a') as csvfile:
                fieldnames=['Airline_name','ICAO','IATA','Callsign','Country','Website']
                writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
                writer.writerow(temp_item)  
        


        i=i+1
        