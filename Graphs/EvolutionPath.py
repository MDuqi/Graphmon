from GraphScript import G
import networkx as nx


def get_evolution_path(from_number, to_number):
    try:
        path = nx.shortest_path(G, source=from_number, target=to_number)
        return path
    except nx.NetworkXNoPath:
        return None