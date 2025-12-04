class Algorithms:
    def __init__(self, graph):
        self.graph = graph

    def greedy_coloring(self):
        colors = ["blue", "green", "red", "yellow", "purple", "orange", "pink", "brown", "gray", "black", "white"]
        for vertex in self.graph.get_vertices():
            if self.graph.get_vertex_color(vertex) is None:
                neighbor_colors = {self.graph.get_vertex_color(neighbor) for neighbor in self.graph.get_neighbors(vertex)}
                for color in colors:
                    if color not in neighbor_colors:
                        self.graph.set_vertex_color(vertex, color)
                        break
        return self.graph.get_chromatic_number()
