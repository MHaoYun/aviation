from py2neo import Graph, Node, Relationship, NodeMatcher
import csv


def database4():
    my_graph = Graph("http://localhost:7474",
                     username="neo4j",
                     password="123456")

    aircraft_types = []
    aircraft_types.append({"Company": "BAC", "Type": "Concorde"})
    aircraft_types.append({"Company": "Mcdonnell Douglas", "Type": "DC-9"})
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
        temp["Company"] = "EMBRAER"
        temp["Type"] = types
        aircraft_types.append(temp)

    for item in aircraft_types:
        type_Node = Node("Aircraft_type",
                         Company=item["Company"],
                         Type=item["Type"])
        my_graph.create(type_Node)

    matcher = NodeMatcher(my_graph)
    targets = list(matcher.match("Plane").where("_.Type=~ '.*Concorde.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="Concorde").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok1")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*220.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A220").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok2")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*300.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A300").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok3")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*310.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A310").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok4")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*318.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A318").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok5")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*319.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A319").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok6")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*320.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A320").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok7")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*321.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A321").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok8")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*330.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A330").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok9")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*340.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A340").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok10")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*350.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A350").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok11")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*380.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A380").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok12")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*A.*400.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="A400").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok13")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*B.*717.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="B717").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok14")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*B.*737.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="B737").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok15")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*B.*747.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="B747").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok16")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*B.*757.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="B757").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok17")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*B.*767.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="B767").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok18")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*B.*777.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="B777").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok19")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*B.*787.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="B787").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok20")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*CRJ.*900.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="CRJ-900").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok21")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*DHC.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="DHC-8").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok22")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*Fokker.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="Fokker-100").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok23")

    targets = list(matcher.match("Plane").where("_.Type=~ '.*DC.*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="DC-9").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok24")

    targets = list(
        matcher.match("Plane").where("_.Type=~ '.*ERJ.*(135|140|145).*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="ERJ-145").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok25")

    targets = list(
        matcher.match("Plane").where("_.Type=~ '.*ERJ.*(170|175).*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="ERJ-170").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok26")

    targets = list(
        matcher.match("Plane").where("_.Type=~ '.*ERJ.*(190|195).*'"))
    for target in targets:
        i = targets.index(target)
        print(str(i) + "/" + str(len(targets)))
        big_type = matcher.match("Aircraft_type", Type="ERJ-190").first()
        is_a = Relationship(target, "Is_a", big_type)
        my_graph.create(is_a)
    print("ok27")


database4()
