from py2neo import Graph, Node, Relationship, NodeMatcher


def database5():
    aircraft_types = []
    aircraft_types.append({"Company": "BAC", "Type": "Concorde"})
    aircraft_types.append({"Company": "McDonnell-Douglas", "Type": "DC-9"})
    aircraft_types.append({"Company": "Fokker", "Type": "Fokker-100"})
    Boeing_types = ["B717", "B737", "B747", "B757", "B767", "B777", "B787"]
    Airbus_types = [
        "A220",
        "A300",
        "A310",
        "A318",
        "A319",
        "A320",
        "A321",
        "A330",
        "A340",
        "A350",
        "A380",
        "A400",
    ]
    Bombardier_types = ["CRJ-100", "CRJ-700", "CRJ-900", "CRJ-1000", "DHC-8"]
    EMBRAER = ["ERJ-145", "ERJ-170", "ERJ-190"]

    for types in Boeing_types:
        temp = {}
        temp["Company"] = "Boeing"
        temp["Type"] = types
        aircraft_types.append(temp)

    for types in Airbus_types:
        temp = {}
        temp["Company"] = "Airbus"
        temp["Type"] = types
        aircraft_types.append(temp)

    for types in Bombardier_types:
        temp = {}
        temp["Company"] = "Bombardier"
        temp["Type"] = types
        aircraft_types.append(temp)
    for types in EMBRAER:
        temp = {}
        temp["Company"] = "Embraer"
        temp["Type"] = types
        aircraft_types.append(temp)

    my_graph = Graph("http://localhost:7474", username="neo4j", password="123456")
    for item in aircraft_types:
        matcher = NodeMatcher(my_graph)
        a = matcher.match("Aircraft_type", Type=item["Type"]).first()
        b = matcher.match("Manufactor", name=item["Company"]).first()
        if b:
            r = Relationship(a, "Manufactured_by", b)
            my_graph.create(r)


database5()
