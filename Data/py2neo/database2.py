from py2neo import Graph, Node, Relationship, NodeMatcher
import csv


def database2():
    my_graph = Graph("http://localhost:7474",
                     username="neo4j",
                     password="123456")

    csvFile = open("Data/py2neo/plane_data_2.csv", "r")
    reader = csv.reader(csvFile)

    i = 0
    for item in reader:
        print(item)
        i = i + 1
        print(i)
        if item[0] != "Aircraft Type":
            node_plane = Node(
                "Plane",
                Type=item[0],
                Register_num=item[2],
                Delivered_date=item[4],
                Status=item[5],
            )
            my_graph.create(node_plane)

            matcher = NodeMatcher(my_graph)
            tar = matcher.match("Manufactor", name=item[1]).first()
            if tar:
                plane_manufactured_by = Relationship(node_plane,
                                                     "Manufactured_by", tar)
                my_graph.create(plane_manufactured_by)
            else:
                node_manufactor = Node("Manufactor", name=item[1])
                my_graph.create(node_manufactor)
                plane_manufactured_by = Relationship(node_plane,
                                                     "Manufactured_by",
                                                     node_manufactor)
                my_graph.create(plane_manufactured_by)

            tar2 = matcher.match("Airline", name=item[3]).first()
            if tar2:
                plane_belong_to = Relationship(node_plane, "Belong_to", tar2)
                my_graph.create(plane_belong_to)
            else:
                node_airline = Node("Airline", name=item[3])
                my_graph.create(node_airline)
                plane_belong_to = Relationship(node_plane, "Belong_to",
                                               node_airline)
                my_graph.create(plane_belong_to)

    print("finished")


database2()
