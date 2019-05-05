import csv
csvFile = open("Data/Aircrafts/plane_data.csv", "r")
reader = csv.reader(csvFile)
f = open('三元组/具体飞机/aircrafts_tri.txt', 'a')
num = 0
for item in reader:
    if item[2] != 'Register number':
        craft_name = '飞机' + item[2]
        tri1 = '<' + craft_name + ',' + '所属机型' + ',' + item[0] + '>\n'
        tri2 = '<' + craft_name + ',' + '制造商' + ',' + item[1] + '>\n'
        tri3 = '<' + craft_name + ',' + '所属公司' + ',' + item[3] + '>\n'
        tri4 = '<' + craft_name + ',' + '交付时间' + ',' + item[4] + '>\n'
        tri5 = '<' + craft_name + ',' + '当前状态' + ',' + item[5] + '>\n'
        num = num + 5
        f.write(tri1)
        f.write(tri2)
        f.write(tri3)
        f.write(tri4)
        f.write(tri5)
        print(num)
