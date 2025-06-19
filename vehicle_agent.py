# vehicle_agent.py

import networkx as nx


class Vehicle:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.path = nx.shortest_path(
            graph, source=start, target=end, weight='weight')
        self.current_position = self.path[0]  # Start at the first node
        self.path_index = 0  # Index to track position on path

    def move(self):
        """
        Moves vehicle one step along the path.
        """
        if self.path_index < len(self.path) - 1:
            self.path_index += 1
            self.current_position = self.path[self.path_index]
        return self.current_position

    def has_arrived(self):
        """
        Returns True if vehicle has reached the destination.
        """
        return self.current_position == self.end
