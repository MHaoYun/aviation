#coding=utf-8
#!/usr/bin/python3
import requests
import json
import datetime
import time
import threading
import urllib
from bs4 import BeautifulSoup
import sys
import codecs
import importlib
importlib.reload(sys)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print('中文')
'''cityAb=['bjs', 'sha', 'can', 'szx', 'ctu', 'hgh', 'wuh', 'sia', 'ckg',
               'tao', 'csx', 'nkg', 'xmn', 'kmg', 'dlc', 'tsn', 'cgo', 'syx',
               'tna', 'foc', 'cgq', 'hrb', 'het', 'nng', 'khn', 'hak', 'lxa',
               'lhw', 'she', 'sjw', 'tyn', 'urc', 'xnn', 'inc', 'hkg', 'mfm']
cityName=['北京', '上海', '广州', '深圳', '成都', '杭州', '武汉', '西安', '重庆',
          '青岛', '长沙', '南京', '厦门', '昆明', '大连', '天津', '郑州', '三亚',
          '济南', '福州', '长春', '哈尔滨', '呼和浩特', '南宁', '南昌', '海口', '拉萨',
          '兰州', '沈阳', '石家庄', '太原', '乌鲁木齐', '西宁', '银川', '香港', '澳门']
		  '''
cityAb=[]
cityName=[]
def getCities():
	page = 0
	request_fail = 0
	try:
			is_next = 0
			url='https://webresource.c-ctrip.com/code/cquery/resource/address/flight/flight_new_poi_gb2312.js'
			# print(url)
			requests_object = requests.get(url, timeout=10)
			# 判断请求是否成功
			if (requests_object.status_code == 200):
				request_fail = 0
				requests_object.encoding = 'gb2312'
				jsonText = requests_object.text
				pos=jsonText.find('suggestion')
				jsonText=jsonText[pos:]
				#print(jsonText)
				cityNamePos=0 #查找城市名字的位置
				abPos0=0 #缩写的前后位置
				abPos1=0
				vCityName=' ' #城市名字 
				vCityAb=' ' #城市缩写
				file = open('cityList.txt','w',encoding='utf-8')
				while jsonText.find("data") >= 0:
					jsonText = jsonText[jsonText.find("data"):]
					cityNamePos=jsonText.find("|")
					abPos0=jsonText.find("(",cityNamePos)
					abPos1=jsonText.find(")",abPos0)
					vCityName=jsonText[cityNamePos+1:abPos0]
					vCityAb=jsonText[abPos0+1:abPos1]
					if abPos1==-1:
						break
					jsonText = jsonText[abPos1:]
					cityName.append(vCityName)
					cityAb.append(vCityAb)
					file.write(vCityName+' '+vCityAb+'\r\n')
				file.close()
			else:
				print('request fail error code is '+str(requests_object.status_code)+ ' ' + str(page))
				if request_fail < 4:
					request_fail += 1
	except:
			print('error '+str(page))
			traceback.print_exc()
	listLength=len(cityAb)
	print("len of cities list:"+str(listLength))
	print("cities list build success")
def crawler(dcId,acId,sDate):
	request_fail = 0
	payloadData = {
	"flightWay":"Oneway","classType":"ALL","hasChild":'false',"hasBaby":'false',"searchIndex":1,"airportParams":[{"dcity":cityAb[dcId],"acity":cityAb[acId],"dcityname":cityName[dcId],"acityname":cityName[acId],"date":sDate}]
	}
	payloadHeader = {
	'accept': '*/*',
	'accept-encoding': 'gzip,deflate,br',
	'accept-language': 'zh-CN,zh;q=0.9',
	'content-length': '225',
    'Content-Type': 'application/json',
	#'cookie': 'DomesticUserHostCity=SHE|%c9%f2%d1%f4; _abtest_userid=4ca1bd11-ed85-49b7-9fbf-5fdb61138084; gad_city=5f1e9e5c1eb7fae5024f3f587fa07e91; _RF1=118.202.41.14; _RSG=Fr4_vFYyFiDiP00Q8qusn8; _RDG=28b44f47f60d39276a1c0a03f503e7c84b; _RGUID=db0ff223-f9fc-4d4f-8c76-e3421a00066c; _ga=GA1.2.959075151.1552563099; _gid=GA1.2.828506205.1552563099; MKT_OrderClick=ASID=4897155934&CT=1552563099281&CURL=https%3A%2F%2Fflights.ctrip.com%2F%3Fallianceid%3D4897%26sid%3D155934%26utm_medium%3Dbaidu%26utm_campaign%3Dpp%26utm_source%3Dbaiduppc%26gclid%3DCJv_3p3EgeECFYROvAod8bcHlw%26gclsrc%3Dds&VAL={"pc_vid":"1552563096482.2raf5p"}; MKT_Pagesource=PC; _gcl_dc=GCL.1552563100.CJv_3p3EgeECFYROvAod8bcHlw; appFloatCnt=2; manualclose=1; FD_SearchHistorty={"type":"S","data":"S%24%u6C88%u9633%28SHE%29%24SHE%242019-04-08%24%u5317%u4EAC%28BJS%29%24BJS"}; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&Expires=1553173866160; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1552569066174%7D%5D; _jzqco=%7C%7C%7C%7C1552563234960%7C1.833720789.1552563099328.1552569037223.1552569066203.1552569037223.1552569066203.undefined.0.0.13.13; __zpspc=9.4.1552569066.1552569066.1%232%7Cwww.baidu.com%7C%7C%7C%7C%23; _bfa=1.1552563096482.2raf5p.1.1552563096482.1552568249767.2.17; _bfs=1.6; _bfi=p1%3D600001375%26p2%3D10320673060%26v1%3D17%26v2%3D16',
	#'host': 'flights.ctrip.com',
	'referer': 'https://flights.ctrip.com/itinerary/oneway/she-bjs?date=2019-04-09',
	#'user-agent': 'Mozilla/5.0 (WindowsNT 10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko) Chrome/72.0.3626.121 Safari/537.36',
	}
	timeOut = 25
	postUrl = "https://flights.ctrip.com/itinerary/api/12808/products"
	r = requests.post(postUrl, data=json.dumps(payloadData), headers=payloadHeader)
	dumpJsonData = json.dumps(payloadData,indent=4)
	#print(f"dumpJsonData = {dumpJsonData}")
	res = requests.post(postUrl, data=dumpJsonData, headers=payloadHeader, timeout=timeOut, allow_redirects=True)
	#print(f"responseTime = {datetime.datetime.now()}, statusCode = {res.status_code}, res text = {res.text}")
	text=res.text.replace('null','""')
	jjj=json.loads(text)
	inpath=cityName[dcId]+'jb.txt'
	uipath=str(inpath).encode("utf-8")
	file = open(uipath,'w',encoding='utf-8')
	file.write(json.dumps(jjj, ensure_ascii=False,indent=2))
	file.close()
	i=0
	inpath='cities/'+sDate+'/'+cityName[dcId]+'.txt'
	uipath=str(inpath).encode("utf-8")
	file = open(uipath,'a',encoding='utf-8')
	file.write('到'+cityName[acId]+':\r\n')
	try:
		while jjj != None and jjj['data']['routeList'] != None:
			if len(jjj['data']['routeList'])>i:
				if 'flight' in jjj['data']['routeList'][i]['legs'][0] and jjj['data']['routeList'][i]['routeType']=='Flight':
					file.write(jjj['data']['routeList'][i]['legs'][0]['flight']['airlineName']+jjj['data']['routeList'][i]['legs'][0]['flight']['flightNumber']+' '+jjj['data']['routeList'][i]['legs'][0]['flight']['craftTypeName']+'('+jjj['data']['routeList'][i]['legs'][0]['flight']['craftTypeKindDisplayName']+')')
					file.write('起飞:'+jjj['data']['routeList'][i]['legs'][0]['flight']['departureAirportInfo']['airportName']+jjj['data']['routeList'][i]['legs'][0]['flight']['departureAirportInfo']['terminal']['shortName'])
					#print(jjj['data']['routeList'][i]['legs'][0]['flight']['airlineName']+jjj['data']['routeList'][i]['legs'][0]['flight']['flightNumber']+' '+jjj['data']['routeList'][i]['legs'][0]['flight']['craftTypeName']+'('+jjj['data']['routeList'][i]['legs'][0]['flight']['craftTypeKindDisplayName']+')', end=' ')
					#print('起飞:'+jjj['data']['routeList'][i]['legs'][0]['flight']['departureAirportInfo']['airportName']+jjj['data']['routeList'][i]['legs'][0]['flight']['departureAirportInfo']['terminal']['shortName'],end=' ')
					time=jjj['data']['routeList'][i]['legs'][0]['flight']['departureDate']
					pos=time.find(' ')
					time=time[pos:]
					#print(time,end=' ')
					file.write(time+' ')
					file.write('降落:'+jjj['data']['routeList'][i]['legs'][0]['flight']['arrivalAirportInfo']['airportName']+jjj['data']['routeList'][i]['legs'][0]['flight']['arrivalAirportInfo']['terminal']['shortName'])
					#print('降落:'+jjj['data']['routeList'][i]['legs'][0]['flight']['arrivalAirportInfo']['airportName']+jjj['data']['routeList'][i]['legs'][0]['flight']['arrivalAirportInfo']['terminal']['shortName'],end=' ')
					time=jjj['data']['routeList'][i]['legs'][0]['flight']['arrivalDate']
					pos=time.find(' ')
					time=time[pos:]
					#print(time)
					file.write(time)
					file.write(' 延误率：'+jjj['data']['routeList'][i]['legs'][0]['flight']['punctualityRate'])
					file.write(' 餐食类型：'+jjj['data']['routeList'][i]['legs'][0]['flight']['mealType'])
					file.write('\r\n')
				i+=1
			else:
				break
	except:
		print('error 出发地点:'+cityName[dcId]+' '+str(dcId)+'到达地点：'+cityName[acId]+str(acId))
		traceback.print_exc()
	file.close()
def start():
	depCityId=0
	arrCityId=0
	searchDate="2019-04-10"
	getCities()
	while depCityId<len(cityAb) and depCityId<285:
		inpath='cities/'+searchDate+'/'+cityName[depCityId]+'.txt'
		uipath=str(inpath).encode("utf-8")
		file = open(uipath,'w',encoding='utf-8')
		file.close()
		time.sleep(5)
		while arrCityId<len(cityAb) and arrCityId<285:
			if arrCityId!=depCityId:
				thread = []
				if(arrCityId+10>len(cityName)):
					end=len(cityName)-1
				else:
					end=arrCityId+10
				for i in range(arrCityId,end):
					print('出发地:'+cityName[depCityId]+'  目的地:'+cityName[i])
					t=threading.Thread(target=crawler,
							args=(depCityId,i,searchDate))
					thread.append(t)
				for i in range(0,len(thread)):
					thread[i].start()
				for i in range(0,len(thread)):
					thread[i].join()
			arrCityId+=10
		depCityId+=1
		arrCityId=0
start()
