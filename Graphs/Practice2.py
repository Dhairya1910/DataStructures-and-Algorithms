class Graph:
    def __init__(self) :
        self.Graph = {}
    def Add_Vertex(self,node):
        if node not in self.Graph:
            self.Graph[node] = []
    def Add_Edge(self,node1,node2):
        self.Graph[node1].append(node2)
    def Display_Graph(self):
        for node in self.Graph:
            print(f"{node}->{self.Graph[node]}")
    
MyGraph = Graph()

MyGraph.Add_Vertex('A')
MyGraph.Add_Vertex('B')
MyGraph.Add_Vertex('C')
MyGraph.Add_Vertex('D')
MyGraph.Add_Vertex('E')

MyGraph.Add_Edge('A','B')
MyGraph.Add_Edge('A','C')
MyGraph.Add_Edge('B','C')
MyGraph.Add_Edge('C','D')
MyGraph.Add_Edge('D','A')

MyGraph.Display_Graph()


