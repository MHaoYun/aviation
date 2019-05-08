import re

file = open('aircraft1.txt', 'w', encoding='utf-8')
aircraft1 = ["B717", "B737", "B747", "B757", "B767", "B777", "B787",
             "CRJ", "ERJ145", "ERJ-170", "EMB-110", "EMB-120", "EMB-121"]
aircraft2 = ["A220", "A300", "A310", "A320", "A330", "A340", "A350",
             "A380", "CRJ", "ERJ145", "ERJ-170", "EMB-110", "EMB-120", "EMB-121"]
aircraft3 = ["CRJ", "ERJ145", "ERJ-170", "EMB-110", "EMB-120", "EMB-121"]

for aircraft in aircraft1:
    fileopen = open(aircraft+'.txt', 'r', encoding='utf-8')
    f = fileopen.read()

    pattern = re.compile(r'波音.*?是(一种)?[^，]*的(一种)?(.*?)[，（]')
    content = re.match(pattern, f)
    if content:
        if content.group(3).find('、'):
            tmp_arr = content.group(3).split('、')
            for arr in tmp_arr:
                file.write('<' + aircraft + ', 类型, ' + arr + '>\n')
        elif content.group(3).find('/'):
            tmp_arr = content.group(3).split('/')
            for arr in tmp_arr:
                file.write('<' + aircraft + ', 类型, ' + arr + '>\n')
        else:
            file.write('<' + aircraft + ', 类型, ' + content.group(3) + '>\n')

    pattern = re.compile(r'(\d{4}年[^，]*[月日]).?(出厂|生产)')
    content = re.search(pattern, f)
    if content:
        file.write('<' + aircraft + ', 出厂时间, ' + content.group(1) + '>\n')

    pattern = re.compile(r'(\d{4}年[^，]*[月日]).?首飞')
    content = re.search(pattern, f)
    if content:
        file.write('<' + aircraft + ', 首飞时间, ' + content.group(1) + '>\n')

    pattern = re.compile(r'(\d{4}年[^，]*?[月日]?)[^，]*投入使用')
    content = re.search(pattern, f)
    if content:
        file.write('<' + aircraft + ', 投入使用, ' + content.group(1) + '>\n')

    pattern = re.compile(r'(\d{4}年.*?日)，(.*?)飞机(成功)?在(.*?)(成功)?完成.*?。')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            file.write('<' + c[1] + ', 首飞时间, ' + c[0] + '>\n')
            file.write('<' + c[1] + ', 首飞地点, ' + c[3] + '>\n')

    pattern = re.compile(r'%s-\d{3}'%aircraft[1:])
    content = re.findall(pattern, f)
    if content:
        for c in set(content):
            file.write('<' + aircraft + ', 包含机型, ' + c + '>\n')

    pattern = re.compile(r'(座位数|座位间距|座位宽度|长度|翼展|高度|后掠翼|展弦比|机身宽|机身高|座舱宽|座舱高|空重'
                         r'|最大起飞重量|基本型|最大降落重量|载货量|MTOW起飞所需跑道长度|实用升限|巡航速率|飞行员数目'
                         r'最大速率|满载航距|最大燃料容量|发动机（x2）|发动机最大推力（x2）|发动机巡航推力（x2）|'
                         r'风扇翼尖直径|发动机长度|发动机离地高度|轮距|航距|最高巡航高度|起飞所需跑道长度（于最大起飞重量时）'
                         r'|最大滑行重量|无燃油最大重量|最大货运容量|机身直径|最大机舱宽度|典型布局载客|续航距离)'
                         r'[\w\W]*?(\d+[,.]?.*?)[，。（\n ]')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            file.write('<' + aircraft + ', ' + c[0] + ', ' + c[1] + '>\n')

    pattern = re.compile(r'(B\d{3}-[^\u4e00-\u9fa5]*?)\n+(\d+)')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            file.write('<' + c[0] + ', 交付数量, ' + c[1] + '>\n')

    pattern = re.compile(r'波音(.*?)型共\d+架：(.*?)[：\n ]')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            tmp_arr = c[1].split('、')
            for arr in tmp_arr:
                begin = arr.find('（') if arr.find('（') != -1 else arr.find('(')
                end = arr.find('）') if arr.find('）') != -1 else arr.find(')')
                type = arr[:begin]
                number = arr[begin+1 : end]
                if begin != -1 and end != -1:
                    file.write('<' + c[0] + ', 有' + number + '架服役于， ' + type + '>\n')

    pattern = re.compile(r'(.*航空(?:有限)?(?:公司)?)[ \n\r]+?(\d+)')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            file.write('<' + aircraft + ', 有' + c[1] + '架服役于， ' + c[0] + '>\n')

    pattern = re.compile(r'\n(\d{4}年.*?)，')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            file.write('<' + aircraft + ', 空难时间， ' + c + '>\n')

    fileopen.close()

for aircraft in aircraft2:
    fileopen = open(aircraft + '.txt', 'r', encoding='utf-8')
    f = fileopen.read()

    pattern = re.compile(r'(空中客车)?'+aircraft+'.*?是(一[个种])?[^，了的]*[了的]?(一[个种])?(.*?)[，（。]')
    content = re.match(pattern, f)
    if content:
        if content.group(4).find('、'):
            tmp_arr = content.group(4).split('、')
            for arr in tmp_arr:
                file.write('<' + aircraft + ', 类型, ' + arr + '>\n')
        elif content.group(3).find('，'):
            tmp_arr = content.group(4).split('，')
            for arr in tmp_arr:
                file.write('<' + aircraft + ', 类型, ' + arr + '>\n')
        else:
            file.write('<' + aircraft + ', 类型, ' + content.group(4) + '>\n')

    pattern = re.compile(r'\n(\d{4}年\w*?[日月])[，\n]+(.*?)[，。]')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            file.write('<' + aircraft + ', ' + c[0] + ', ' + c[1] + '>\n')

    pattern = re.compile(r'，(\d{4}年.*?)(开始研制|投入生产)')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            file.write('<' + aircraft + ', ' + c[1] + ', ' + c[0] + '>\n')

    pattern = re.compile(r'.*?([-\w]*?%s[-\w]*)[：\n]'%aircraft, re.A)
    content = re.findall(pattern, f)
    if content:
        for c in set(content):
            if c != aircraft:
                file.write('<' + aircraft + ', 包含机型, ' + c + '>\n')

    pattern = re.compile(r'(总长度|高度|翼展|机身直径|客舱长度|客舱最大宽度|典型两级座舱布局|全经济布局载客|'
                         r'货舱容积|巡航速度|经济巡航速度|经济巡航高度|最大燃油容量|空重|最大起飞重量|'
                         r'起飞所需跑道长度|满载航距|机师数|机长|机高|主轮距|最小转弯半径|爬升率'
                         r'发动机型号|发动机台数|Tsh|发动机推力（马力）|45度侧风（m/s）|90度侧风（m/s）|'
                         r'最大起飞重量（Kg）|最大着陆重量|最大无油重量|最大业载|最大载油量|燃油容量|'
                         r'平均小时耗油量|最大爬升率（ft/min）|最大爬升率（m/s）|最大下降率（ft/min）|'
                         r'最大下降率（m/s）|实用升限（m）|着陆距离（m）|满载最大航程（Km）|ACN值|'
                         r'最大巡航速度（Kts）|最大巡航速度（Km/h）|最大巡航速度（M）|正常巡航速度（Kts）|'
                         r'正常巡航速度（Km/h）|正常巡航速度（M[)）]|最小光洁速度（Kts）|最小光洁速度（Km/h）|'
                         r'最后进近速度（Kts）|最后进近速度（Km/h）|跑道入口速度（Kts）|跑道入口速度（Kts,Km/h）|'
                         r'宽度|载货量|空机重|最大商载|最大起飞总重|最大燃油量|最大可用燃油|动力装置|可选发动机型号|'
                         r'实用升限|涡扇引擎|后掠翼角度|轮基距|轮轨距|标准座席数|最大结构重量|标准营运空重|'
                         r'标准货运载重|货运载酬|操作空重|起飞滑跑距离|航距|发动机推力|推重比|'
                         r'现役飞机总数|单位造价|生产公司|首次飞行|首次服役|使用状态)'
                         r'[\w\W]*?(\d+[,.]?.*?)[，。（\n ]')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            file.write('<' + aircraft + ', ' + c[0] + ', ' + c[1] + '>\n')

    pattern = re.compile(r'\n(.*?航空)[\n：]+(\d+)')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            file.write('<' + aircraft + ', 有' + c[1] + '架服役于， ' + c[0] + '>\n')

    pattern = re.compile(r'(.*?航空公司)([\d\n]+)')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            tmp_arr = c[1].split('\n\n')
            for arr in tmp_arr:
                if arr:
                    file.write('<' + aircraft + ', 飞机编号, ' + c[0] + arr + '>\n')

    fileopen.close()

for aircraft in aircraft3:
    fileopen = open(aircraft + '.txt', 'r', encoding='utf-8')
    f = fileopen.read()

    pattern = re.compile(r'(\d{4}年\d+月\d+日)\s?(.*?)[：\s]')
    content = re.findall(pattern, f)
    if content and re.match(r'EMB-110|EMB-120', aircraft):
        for c in content:
            file.write('<' + aircraft + ', 空难时间, ' + c[0] + '>\n')
            file.write('<' + aircraft + ', 空难地点, ' + c[1] + '>\n')

    pattern = re.compile(r'(.*航空)(\d+)架')
    content = re.findall(pattern, f)
    if content:
        for c in content:
            file.write('<' + aircraft + ', 有' + c[1] + '架服役于， ' + c[0] + '>\n')

    fileopen.close()

