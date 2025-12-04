from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(set)
        self.directed = directed
        self.vertices = set()
        self.colors = {}
    
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
        if vertex not in self.graph:
            self.graph[vertex] = set()
    
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].add(v)
        if not self.directed:
            self.graph[v].add(u)
    
    def get_neighbors(self, vertex):
        return list(self.graph.get(vertex, set()))

    def get_vertex_degree(self, vertex):
        return len(self.get_neighbors(vertex))
    
    def get_vertices(self):
        return list(self.vertices)
    
    def get_edges(self):
        edges = []
        visited = set()
        for u in self.graph:
            for v in self.graph[u]:
                if not self.directed:
                    if (v, u) not in visited:
                        edges.append((u, v))
                        visited.add((u, v))
                else:
                    edges.append((u, v))
        return edges
    
    def get_vertex_color(self, vertex):
        return self.colors.get(vertex, None)
    
    def get_chromatic_number(self):
        chromatic_number = 0
        used_colors = set()
        for color in self.colors.values():
            if color is not None and color not in used_colors:
                used_colors.add(color)
                chromatic_number += 1
        return chromatic_number
    
    def set_vertex_color(self, vertex, color):
        self.colors[vertex] = color

    def __repr__(self):
        return f"Graph(directed={self.directed}, vertices={len(self.vertices)}, edges={len(self.get_edges())})"