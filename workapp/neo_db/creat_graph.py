from py2neo import Graph, Node, Relationship,NodeSelector
from config import graph

with open("../static/personrelkg.txt",'r',encoding='UTF-8') as f:
    for line in f.readlines():
        rela_array=line.strip("\n").split(",")
        print(rela_array)
        graph.run("MERGE(p: Person{Name: '%s'})"%(rela_array[0]))
        graph.run("MERGE(p: Person{Name: '%s'})" % (rela_array[3]))
        graph.run(
            "MATCH(e: Person), (cc: Person) \
            WHERE e.Name='%s' AND cc.Name='%s'\
            CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
            RETURN r" % (rela_array[0], rela_array[3], rela_array[1],rela_array[2])

        )
        
