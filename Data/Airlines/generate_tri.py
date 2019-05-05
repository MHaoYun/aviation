import csv
csvFile = open("Data/Airlines/airline_data.csv", "r")
reader = csv.reader(csvFile)
f = open('三元组/航空公司/airline_tri.txt', 'a')
num = 0
for item in reader:
    if item[1] != 'ICAO':
        name = item[0]
        tri = []
        if item[1]:
            tri.append('<' + name + ',' + 'ICAO编码' + ',' + item[1] + '>\n')
        if item[2]:
            tri.append('<' + name + ',' + 'IATA编码' + ',' + item[2] + '>\n')
        if item[3]:
            tri.append('<' + name + ',' + '电台呼叫码' + ',' + item[3] + '>\n')
        if item[4]:
            tri.append('<' + name + ',' + '所在国家' + ',' + item[4] + '>\n')
        if item[5]:
            tri.append('<' + name + ',' + '网址' + ',' + item[5] + '>\n')
        for i in tri:
            f.write(i)
        num = num + len(tri)
        print(num)
