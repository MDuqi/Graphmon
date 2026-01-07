import sqlite3
import networkx as nx

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

conn.close()
#print(G.nodes)
