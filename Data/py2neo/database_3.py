from py2neo import Graph

my_graph = Graph("http://localhost:7474", username="neo4j", password="123456")
my_graph.delete_all()
