from Graph import Graph
from Algorithms import Algorithms

g = Graph(directed=False)

edges = [
    ('A', 'B'), ('A', 'C'), 
    ('B', 'D'), ('B', 'E'),
    ('C', 'D'), ('C', 'E'),
    ('D', 'E')
]

for u, v in edges:
    g.add_edge(u, v)

print(f"Graph: {g}")
print(f"Vertices: {g.get_vertices()}")
print("\nEdges:")
for u, v in g.get_edges():
    print(f"  {u} -- {v}")

algorithms = Algorithms(g)
print(algorithms.greedy_coloring())