from GraphScript import G
import matplotlib.pyplot as plt
import networkx as nx


if nx.is_connected(G):  # Check if the graph is strongly connected
    print("It's possible to reach any Digimon from any other Digimon.")
else:
    print("It's NOT possible to reach any Digimon from any other Digimon.")

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")
plt.title("Digimon Evolution Graph")
plt.show()

