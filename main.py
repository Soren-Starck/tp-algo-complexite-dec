from Graph import Graph


g = Graph(directed=False)

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

print(f"Graph: {g}")
print(f"Vertices: {g.get_vertices()}")
print(f"\nEdges:")
for u, v in g.get_edges():
    print(f"  {u} --> {v}")

print(f"\nNeighbors of 'B': {g.get_neighbors('B')}")
