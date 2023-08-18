"""
Author: Pol Marin

Implementation of a Graph class using networkx

"""

import networkx as nx
import matplotlib.pyplot as plt

class Graph():

    def __init__(self, graph_dict: dict = None, initial_node: str = None, end_node: str = None):
        self.G = nx.Graph()
        self.initial_node = initial_node if initial_node is not None else [*graph_dict.keys()][0]
        self.end_node = end_node if end_node is not None else [*graph_dict.keys()][-1]

        if graph_dict:
            self.__create_graph(graph_dict)  

    def __create_graph(self, graph_dict: dict):
        # Create graph and add nodes
        
        self.G.add_nodes_from(graph_dict.keys())

        for node in graph_dict.keys():
            for connected_node in graph_dict[node]:
                self.G.add_edge(node, connected_node)

    def show_graph(self, visited: set = None, save: bool = False, filename: str = ''):
        # Print graph info
        print(self.G)

        # Prepare plot
        color_map = ['#ECEAE4']*len(self.G)
        for i, node in enumerate(self.G):
            if node == self.initial_node:
                color_map[i] = '#CCE2CB'
            elif node == self.end_node:
                color_map[i] = '#FD8A8A'
            elif visited and node in visited:
                color_map[i] = '#FFFFBA'
        
        nx.draw(self.G, node_color=color_map, with_labels=True)

        if save:
            assert filename != '', 'Provide a file name for the plot to be saved, please'
            plt.savefig(filename)

        plt.show()

    



