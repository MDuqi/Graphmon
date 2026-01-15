import sqlite3
import networkx as nx

# create graph
# G = nx.Graph()
D = nx.DiGraph()
Nums = []

# connect to db and get all digimon numbers
conn = sqlite3.connect('DB/Digimon.db')
cursor = conn.cursor()

Nums = cursor.execute("SELECT Number, StageLevel FROM digimon")

# add nodes to graph based on digimon numbers
for Num in Nums:
    D.add_node(Num[0], layer=Num[1])


for node in D.nodes:
    from_number = node
    Evolutions = cursor.execute(
        "SELECT ToNumber FROM evolution WHERE FromNumber = ?", (from_number,))
    for Evo in Evolutions:
        D.add_edge(from_number, Evo[0])
        # add reverse edge for the de-digivolution
        D.add_edge(Evo[0], from_number)

conn.close()
