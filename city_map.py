# city_map.py

import networkx as nx
import random


def create_city_grid(size=5):
    """
    Creates a grid-like city map using NetworkX.
    Each node is an intersection (x, y), and each edge is a road.
    """
    # Create a 2D grid graph (like a city layout)
    G = nx.grid_2d_graph(size, size)

    # Convert to directional graph to simulate one-way streets (optional)
    G = nx.DiGraph(G)

    # Optionally add weights (like travel time or congestion)
    for (u, v) in G.edges():
        G[u][v]['weight'] = 1  # can change this dynamically later

    return G


def get_random_nodes(G):
    """
    Picks two random, different intersections (nodes) from the graph.
    Useful for simulating vehicle routes.
    """
    nodes = list(G.nodes)
    start = random.choice(nodes)
    end = random.choice(nodes)
    while end == start:
        end = random.choice(nodes)
    return start, end
