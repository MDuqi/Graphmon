import sqlite3
import networkx as nx
import matplotlib.pyplot as plt

#create graph
G = nx.Graph()
Nums = []

#connect to db and get all digimon numbers
conn = sqlite3.connect('DB/Digimon.db')
cursor = conn.cursor()

Nums = cursor.execute("SELECT number FROM digimon")

#add nodes to graph based on digimon numbers
for Num in Nums:
    G.add_node(Num[0])

for node in G.nodes:
    from_number = node
    Evolutions = cursor.execute("SELECT ToNumber FROM evolution WHERE FromNumber = ?", (from_number,))
    for Evo in Evolutions:
        G.add_edge(from_number, Evo[0])

conn.close()

#draw graph
nx.draw(G, with_labels=True)
plt.show()

#print(G.nodes)
#print(G.edges)
