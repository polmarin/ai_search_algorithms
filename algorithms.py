"""
Author: Pol Marin

AI Search Algorithm implementations are hold here:
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Greedy Best-First Search (GBFS)
- A* Search

"""

import networkx as nx
from graph import Graph

#################################
###########    DFS    ###########
#################################
def dfs(graph: Graph, 
        start: str, 
        end: str,
        visited: set = set() 
        ): 
    """ Recursive DFS implementation """
    if start not in visited:

        # We check if the current node is the one for which we are looking for
        visited.add(start)
        if start == end:
            return visited

        for neighbor in graph.G[start]:
            # If we found the node, we break out from the loop
            if dfs(graph, neighbor, end):
                return visited
        # If we did not find the node we were looking for, we return False
        return False
    

#################################
###########    BFS    ###########
#################################

def bfs(graph: Graph, 
        start: str, 
        end: str
        ):
  
    """ Iterative BFS implementation """
    visited = [start]
    queue = [start]

    neighbor = start

    while queue and neighbor != end:
        m = queue.pop(0) 
        print (m, end = " ") 

        for neighbor in graph.G[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                if neighbor == end:
                    break

    return visited


#################################
##########    GBFS    ###########
#################################
def gbfs(graph: Graph, 
        start: str, 
        end: str,
        heuristics: dict
        ):
    
    """ GBFS using a recursive function """
    
    # Set node weights
    nx.set_node_attributes(graph.G, heuristics, "h")

    print(start, end)
    
    return rec_gbfs(graph, start, end, set())

def rec_gbfs(graph: Graph, 
             start: str, 
             end: str,
             visited: set = set() 
             ):
    
    if start not in visited:

        # We check if the current node is the one for which we are looking for
        visited.add(start)
        if start == end:
            return visited
        
        neighbors = sorted(graph.G[start], key=lambda n: graph.G.nodes[n]['h'])
        for neighbor in neighbors:
            # If we found the node, we break out from the loop
            if rec_gbfs(graph, neighbor, end, visited):
                return visited
        # If we did not find the node we were looking for, we return False
        return False
    

#################################
############    A*    ###########
#################################

# ...
# This one is empty so the user can code it using the previous code snippets as reference.
def a_star(graph: Graph, 
           start: str, 
           end: str,
           edge_weights: dict,
           heuristics: dict = None, # Optional because we might have already set them
           ):
    pass