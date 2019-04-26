import re
import traceback  
from py2neo import Node, Relationship,Graph,NodeMatcher
def conn():
	try:
		graph = Graph("http://localhost:7474")
		if(graph):
			print("Database connection successful")
			return graph
	except :
		print("Database connection failed")
		traceback.print_exc()
def propertySet(graph,contnt,nodeA):
	if(contnt!=None):
		if contnt.group(1)=="类型":
			if contnt.group(2) == "小型":
				kind = 'S'
			elif contnt.group(2) == "中型":
				kind = 'M'
			elif contnt.group(2) == "大型":
				kind = 'L'
			else:
				kind = 'null'
			nodeA['craftKind']=kind
		elif contnt.group(1)=="延误率":
			nodeA['punctualityRate']=contnt.group(2)
		elif contnt.group(1)=="餐食":
			nodeA['mealType']=contnt.group(2)
		elif contnt.group(1)=="起飞时间":
			nodeA['departureTime']=contnt.group(2)
		elif contnt.group(1)=="降落时间":
			nodeA['arrivalTime']=contnt.group(2)
		else :
			relationSet(graph,nodeA,contnt.group(2),contnt.group(1))
	return nodeA
def relationSet(graph,flight,airport,type): #负责航班和机场之间的关系
	matcher = NodeMatcher(graph)
	iatac = arpotNamToIATA(airport)
	result = matcher.match("Airport", IATA_code=iatac).first()
	if(type.find("起飞")):
		relationName = 'departsFrom'
	else:
		relationName = 'ArriveAt'
	if result != None:
		r = Relationship(flight, relationName, result)
		graph.create(r)
def arpotNamToIATA(name):
	IATAFile = open('ChineseAirportIATA.txt','r',encoding='utf-8')
	txt = IATAFile.read()
	IATA = "none"
	name = re.sub('[a-zA-Z0-9]','',name)
	if txt != None:
		locate = txt.find(name)
		if locate>0 :
			while(txt[locate-1]!='	'):
				locate=locate-1
			IATA = txt[locate-9:locate-6]
	IATAFile.close()
	return IATA
def airlineIA2IC(iata):
	file = open('AirlineName.txt','r',encoding='utf-8')
	txt = file.read()
	if txt != None:
		locate = txt.find(iata)
		ICAO = txt[locate+3:locate+6]
	file.close()
	return ICAO
def sampleBuild(graph,txtPoses): #此处airline指航班号
	airline = re.search( r'<([\u4e00-\u9fa5]*)(\w*),', txtPoses, re.M|re.I)
	content = re.search( r'(\w*),([\w:%]*)>', txtPoses, re.M|re.I)
	if airline:
		print ("#", airline.group(1), airline.group(2))
		matcher = NodeMatcher(graph)
		result = matcher.match("Flight", name=airline.group(2)).first()
		if result == None:
			print("Creating the node:",airline.group(2))
			flight=Node('Flight',name=airline.group(2))
			propertySet(graph,content,flight)
			try:
					graph.create(flight)
					matcher = NodeMatcher(graph)
					airlineIATA = airline.group(2)[:2]
					airlineICAO = airlineIA2IC(airlineIATA)
					result = matcher.match("Airline", ICAO=airlineICAO,Country='China').first()
					if result != None:
						r = Relationship(flight, 'BelongsTo', result)
						graph.create(r)
					print("successful")
			except :
				print("failed")
				traceback.print_exc()
		else:
			print("Node:",airline.group(2)," found")
			propertySet(graph,content,result)
			graph.push(result)
def main():
	graph=conn()
	if(graph):
		try:
			file = open('ticketsTO3/to3-8.txt','r',encoding='utf-8')
			'''airportNode = Node('Airport',name ='万州五桥机场' ,IATA_code='WXN')
			graph.create(airportNode)
			airportNode2 = Node('Airport',name ='咸阳国际机场' ,IATA_code='XIY')
			graph.create(airportNode2)
			airlineNode = Node('Airline',Airline_name ='Sichuan Airlines' ,IATA='3U',ICAO='CSC',Country='China')
			graph.create(airlineNode)
			airlineNode2 = Node('Airline',Airline_name ='Air China' ,IATA='CA',ICAO='CCA',Country='China')
			graph.create(airlineNode2)'''
			if file:
				txt=file.readline()
				while txt!=None:
					sampleBuild(graph,txt)
					txt=file.readline()
			file.close()
		except :
			print("file open failed")
			traceback.print_exc()
main()
