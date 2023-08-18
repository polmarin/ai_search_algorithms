"""
Author: Pol Marin

Main code putting all the algorithms into work

"""

from algorithms import dfs, bfs, gbfs, a_star
from graph import Graph

# Setup graph: each key is a node and the values set contains the connected nodes
graph = {
    'A': set(['B']),
    'B': set(['C', 'F']),
    'C': set(['E']),
    'D': set(['E']),
    'E': set([]),
    'F': set(['D', 'E'])
}
g = Graph(graph, initial_node = 'A', end_node = 'E')

# Run DFS and paint visited in graph
path = dfs(g, g.initial_node, g.end_node)
print("Visited nodes using the DFS algorithm:", path)
g.show_graph(path, True, 'dfs.png')

# Run BFS and paint visited in graph
path = bfs(g, g.initial_node, g.end_node)
print("Visited nodes using the BFS algorithm:", path)
g.show_graph(path, True, 'bfs.png')

# Prepare heuristics for GBFS: each node has an associated h value
heuristics = {
    'A': 2,
    'B': 2, 
    'D': 3,
    'C': 10,
    'E': 0,
    'F': 4
}

# Run GBFS and paint visited in graph
path = gbfs(g, g.initial_node, g.end_node, heuristics)
print("Visited nodes using the GBFS algorithm:", path)
g.show_graph(path, True, 'gbfs.png')

# Prepare backward (edge) weights for A*: each edge has an associated weight
edge_weights = {
    ('A', 'B'): 2,
    ('B', 'C'): 5,
    ('B', 'F'): 1,
    ('C', 'E'): 2,
    ('F', 'E'): 10,
    ('F', 'D'): 3,
    ('D', 'E'): 1
}

# Run A* and paint visited in graph
path = a_star(g, g.initial_node, g.end_node, edge_weights)
print("Visited nodes using the A* algorithm:", path)
g.show_graph(path, True, 'a_star.png')