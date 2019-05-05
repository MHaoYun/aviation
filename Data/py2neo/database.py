from py2neo import Graph, Node, Relationship, NodeMatcher
import csv


def database1():
    my_graph = Graph("http://localhost:7474",
                     username="neo4j",
                     password="123456")

    csvFile = open("Data/py2neo/airline_data.csv", "r")
    reader = csv.reader(csvFile)
    for item in reader:
        print(item)

        if item[0] != "Airline":
            node_airline = Node("Airline",
                                name=item[0],
                                ICAO=item[1],
                                IATA=item[2],
                                Callsign=item[3])
            if item[5] != "":
                node_airline.update(website=item[5])
            my_graph.create(node_airline)

            matcher = NodeMatcher(my_graph)
            tar = matcher.match("Country", name=item[4]).first()
            if tar:
                airline_locates_in = Relationship(node_airline, "locate", tar)
                my_graph.create(airline_locates_in)
            else:
                node_country = Node("Country", name=item[4])
                my_graph.create(node_country)
                airline_locates_in = Relationship(node_airline, "locate",
                                                  node_country)
                my_graph.create(airline_locates_in)


database1()
