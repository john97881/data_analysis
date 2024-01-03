import sys

#Class representing a Vertex in the graph
class Vertex:
    def __init__(self, node):
        #Unique identifier for the vertex
        self.id = node
        #Dictionary to store adjacent vertices and their weights
        self.adjacent = {}
        #Set distance to infinity for all nodes
        self.distance = sys.maxsize
        #Mark all nodes as unvisited
        self.visited = False
        #Predecessor vertex
        self.previous = None

    #Method to add a neighbor to the current vertex
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    #Method to get the adjacent vertices
    def get_connections(self):
        return self.adjacent.keys()

    #Method to get the unique identifier of the vertex
    def get_id(self):
        return self.id

    #Method to get the weight of the edge to a specific neighbor
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    # Method to represent the vertex as a string
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

#Class representing the Graph
class Graph:
    def __init__(self):
        # Dictionary to store vertices in the graph
        self.vert_dict = {}
        # Counter for the number of vertices
        self.num_vertices = 0

    #Method to iterate over vertices in the graph
    def __iter__(self):
        return iter(self.vert_dict.values())

    #Method to add a vertex to the graph
    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    #Method to get a vertex by its unique identifier
    def get_vertex(self, n):
        return self.vert_dict.get(n, None)

    #Method to add an edge between two vertices with an optional cost
    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        #Adding the edge in both directions since it's an undirected graph
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    #Method to get the unique identifiers of all vertices in the graph
    def get_vertices(self):
        return self.vert_dict.keys()


#Main execution block
if __name__ == '__main__':
    #Creating an instance of the Graph class
    g = Graph()

    # Adding vertices to the graph
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    #Adding edges with their respective weights
    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    #Displaying the graph data
    print('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))
