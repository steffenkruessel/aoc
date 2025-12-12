class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return self._graph_dict[vertice]

    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        #for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
        for x, y in [(vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].append(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj

    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex
            in graph """
        if path == None:
            path = []
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

class Device:
    def __init__(self, device_details):
        self.id = device_details[0]
        self.connections = device_details[1]

class Rack:
    def __init__(self):
        self.devices = []
        self.connection_count = 0
        self.path = Graph()
        self.graph = {}

    def add(self, device):
        # using an array for a graph representation
        self.devices.append(device)

        # using Graph class
        self.path.add_vertex(device.id)
        for connection in device.connections:
            self.path.add_edge({device.id, connection})

        # use a set for storing a graph representation
        self.graph.update({device.id: device.connections})

        # count connections just for some statistics
        self.connection_count += len(device.connections)

    # unfolds all connections hidden behind the devices
    def get_all_connections(self):
        connections = []
        for device in self.devices:
            for connection in device.connections:
                connections.append([device.id, connection])
        #print("All connections:", connections)
        return connections

    # returns the number of paths for a certain route in a given set of connections
    def paths(self, start, end, connections):
        number = 0

        if len(connections) <= 0:
            return 0

        #print("Looking for paths between {} and {} in {}".format(start, end, connections))

        for connection_index in range(len(connections)):
            if connections[connection_index][1] == end:
                if connections[connection_index][0] == start:
                    return 1

                print("Path found between {} and {}".format(connections[connection_index][0], connections[connection_index][1]))
                number += self.paths(start, connections[connection_index][0], connections[0:connection_index]+connections[connection_index+1:])

        return number

    # search through graph (forward)
    def find_all_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if not start in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
# create a "Rack"
rack = Rack()
with open("input.txt", "r") as file:
    for line in file:
        # device ID
        device = [line.strip("\n\r").split(": ")[0]]

        # connections for this device ID
        connections = line.strip("\n\r").split(": ")[1]
        rack_connections = []
        for connection in connections.split(" "):
            rack_connections.append(connection)
        device.append(rack_connections)

        print("Device", device[0], "connected to", device[1])
        rack.add(Device(device))

# "solve" the Rack
print("Given", rack.connection_count, "connections...")
print(rack.graph)

number_of_paths = 0
# fft is always first
# dac to out (5034 solutions)
solutions = rack.find_all_paths("svr", "out")

for solution in solutions:
    if ("dac" in solution) & ("fft" in solution):
        number_of_paths += 1
print("Solution:", number_of_paths)
