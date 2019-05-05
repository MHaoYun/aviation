from py2neo import Graph, Node, Relationship, NodeMatcher
import csv
import re


def database6():
    my_graph = Graph("http://localhost:7474",
                     username="neo4j",
                     password="123456")

    csvFile = open("Data/py2neo/wiki_disasters.csv", "r")
    reader = csv.reader(csvFile)

    for item in reader:
        print(item)
        disaster = Node('Disaster', name=item[0], time=item[1])
        if item[2]:
            disaster.update(Death_toll=item[2])
        if item[3]:
            disaster.update(Wounded=item[3])
        if item[4]:
            disaster.update(Survivor=item[4])
        if item[5]:
            disaster.update(Aircraft_type=item[5])
        my_graph.create(disaster)
    matcher = NodeMatcher(my_graph)
    targets = list(matcher.match("Aircraft_type").where("_.Type=~ '.*A.*'"))
    for target in targets:
        name = target['Type']
        #print(name)
        # temp = re.match('A(.*)', name)
        # print(temp.group(0))

        temp = re.search('A(.*)', name, re.S)
        name = temp.group(1)

        regular = "_.Aircraft_type=~'.*A" + name + ".*'"
        print(regular)
        disasters = list(matcher.match("Disaster").where(regular))
        for disaster in disasters:
            invovle = Relationship(target, 'Involved in', disaster)
            my_graph.create(invovle)

    targets = list(matcher.match("Aircraft_type").where("_.Type=~ '.*B.*'"))
    for target in targets:
        name = target['Type']
        print(name)
        temp = re.match('B(.*)', name)
        if temp:
            print(temp.group(0))

        temp = re.search('B(.*)', name, re.S)
        name = temp.group(1)

        regular = "_.Aircraft_type=~'.*" + name + ".*'"
        print(regular)
        disasters = list(matcher.match("Disaster").where(regular))
        for disaster in disasters:
            invovle = Relationship(target, 'Involved in', disaster)
            my_graph.create(invovle)


database6()
