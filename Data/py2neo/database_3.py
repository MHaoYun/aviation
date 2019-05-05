from py2neo import Graph

print('ok')
my_graph = Graph("http://localhost:7474", username="neo4j", password="123456")
print('ok')
my_graph.delete_all()
print('ok')
