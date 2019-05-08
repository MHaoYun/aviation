import os
import re
import traceback  
def start():
	cityFlight = open("cityFlight.txt",'w',encoding='utf-8')
	cityFlight.close()
	date = "2019-04-"
	day = 8
	dayStr=""
	while(day <= 14):
		if(day<10):
			dayStr='0'+str(day)
		else:
			dayStr=str(day)
		dirPath = "cities/"+date+dayStr+"/"
		list = os.listdir(dirPath)
		to3File = open("to3-"+str(day)+".txt",'w',encoding='utf-8')
		to3File.close()
		for i in range(0,len(list)):
			path = os.path.join(dirPath,list[i])
			city =  re.sub('[a-zA-Z0-9.]','',list[i])
			if os.path.isfile(path):
				to3(path,day,city)
		day=day+1
def ifValid(str):
	if str!="" and str!=" ":
		return True
	return False
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
def arpotNam2CtyNam(name):
	city = "none"
	IATAFile = open('cityList.txt','r',encoding='utf-8')
	txt = IATAFile.readline()
	while  txt!=None:
		pos = txt.find(" ")
		txt = txt[:pos]
		if name.find(txt):
			city = txt
			return city
		txt = IATAFile.readline()

def airlineIA2IC(iata):
	file = open('AirlineName.txt','r',encoding='utf-8')
	txt = file.read()
	if txt != None:
		locate = txt.find(iata)
		ICAO = txt[locate+3:locate+6]
	file.close()
	return ICAO
def to3(path,i,city):
	file = open(path,'r',encoding='utf-8')
	to3File = open("to3-"+str(i)+".txt",'a',encoding='utf-8')
	cityFlight = open("cityFlight.txt",'a',encoding='utf-8')
	flight=""
	modal=""
	planeType=""
	delayRate=""
	mealType=""
	dpAirport=""
	arrAirport=""
	dpTime=""
	arrTime=""
	for line in file:
		if line[0]!="到" :
			flight= line[0:line.find(" ")]
			if line.find("(") != (line.find(")") - 1):
				modal = line[line.find(" ")+1:line.find("(")]
				planeType = line[line.find("(")+1:line.find(")")]
			delayRate = line[line.find("延误率")+4:line.find("餐食类型")-1]
			mealType = line[line.find("餐食类型：")+5:len(line)-1]
			line = line[line.find("起飞:")+3:]
			dpAirport = line[:line.find(" ")]
			dpTime = line[line.find(" ")+1:line.find("降落:")-1]
			line = line[line.find("降落:")+3:]
			print(line)
			arrAirport = line[:line.find(" ")]
			arrTime = line[line.find(" ")+1:line.find("延误率：")-1]
			if ifValid(flight): 	
				'''if ifValid(modal):
					to3File.write("<"+flight+",机型,"+modal+">")
					to3File.write('\n')
				if ifValid(planeType):
					to3File.write("<"+flight+",类型,"+planeType+">")
					to3File.write('\n')
				if ifValid(delayRate):
					to3File.write("<"+flight+",延误率,"+delayRate+">")
					to3File.write('\n')
				if ifValid(mealType):
					to3File.write("<"+flight+",餐食,"+mealType+">")
					to3File.write('\n')
				if ifValid(dpTime):
					to3File.write("<"+flight+",起飞时间,"+dpTime+">")
					to3File.write('\n')
				if ifValid(arrTime):
					to3File.write("<"+flight+",降落时间,"+arrTime+">")
					to3File.write('\n')'''
				if ifValid(dpAirport):
					to3File.write("<"+flight+",起飞机场,"+arpotNamToIATA(dpAirport)+">")
					to3File.write('\n')
				if ifValid(arrAirport):
					to3File.write("<"+flight+",降落机场,"+arpotNamToIATA(arrAirport)+">")
					to3File.write('\n')
					if ifValid(arrAirport) and ifValid(dpAirport):
						cityFlight.write("<"+city+","+flight+","+arpotNam2CtyNam(dpAirport)+">")
						cityFlight.write('\n')

	file.close()
	cityFlight.close()
	to3File.close()
start()