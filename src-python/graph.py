class Graph:
    """
    Implements a simple graph
    """
    def __init__(self, vertices):
        self.vertices = set(vertices)
        self.adj_lists = {}
        for vertex in vertices:
            self.adj_lists[vertex] = []
    
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
    
    def add_edge(self, vertex1, vertex2):
        if not (vertex1 in self.vertices) or not (vertex2 in self.vertices):
            raise ValueError("vertex not in graph")
        self.adj_lists[vertex1].append(vertex2)
        self.adj_lists[vertex2].append(vertex1)

    def delete_vertex(self, vertex):
        self.vertices.remove(vertex)

    def delete_edge(self, vertex1, vertex2):
        pass

    def degree(self, vertex):
        pass

    def get_neighbors(self, vertex):
        pass


class DirectedWeightedGraph: 
    """
    Implements a directed weighted graph
    """
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}
        for vertex in vertices:
            self.adj_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight):
        if not (vertex1 in self.vertices) or not (vertex2 in self.vertices):
            raise ValueError("vertex not in graph")
        self.adj_list[vertex1].append((vertex2, weight))

    def get_edges(self):
        for vertex in self.vertices:
            for edge in self.adj_list[vertex]:
                yield (vertex, edge[0], edge[1])

    def get_vertices(self):
        return self.vertices

