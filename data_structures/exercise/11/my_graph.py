class Graph:
    def __init__(self) -> None:
        self.length = 0
        self.nodes_dic = {}

    def add_vertex(self, node):
        self.nodes_dic[node] = []
        self.length += 1

    def add_edge(self, node1, node2):
        if node2 not in self.nodes_dic[node1]:
            self.nodes_dic[node1].append(node2)
        if node1 not in self.nodes_dic[node2]:
            self.nodes_dic[node2].append(node1)

    def show_vertex(self):
        for key, value in self.nodes_dic.items():
            print(f"{key} --> ", end="")
            for val in value:
                print(f"{val} ", end="")
            print()


my_graph = Graph()
my_graph.add_vertex(0)
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)
my_graph.add_vertex(6)

my_graph.add_edge(3, 1)
my_graph.add_edge(3, 4)
my_graph.add_edge(4, 2)
my_graph.add_edge(4, 5)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 0)
my_graph.add_edge(3, 1)
my_graph.add_edge(0, 2)
my_graph.add_edge(6, 5)

my_graph.show_vertex()
