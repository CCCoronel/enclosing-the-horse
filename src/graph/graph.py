class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, u):
        if u not in self.adj:
            self.adj[u] = {}

    def add_edge(self, u, v, capacity):
        self.add_node(u)
        self.add_node(v)
        self.adj[u][v] = capacity
