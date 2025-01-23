# using inbuild Library 
from collections import defaultdict

class Graph:
    def __init__(self) :
        self.Graph = defaultdict(list)
    
    def add_edge(self,node1,node2):
        self.Graph[node1].append((node2))
    
    def display_graph(self):
        for node in self.Graph:
            print(f"{node} -> {self.Graph[node]}")
    
    def Depth_First_Search(self):
        seen = set()
        visit = ['A']
        source = 'A'
        seen.add(source)
        while visit:
            curr = visit.pop()
            print(curr)
            for Neigbhour in self.Graph[curr]:
                if Neigbhour not in seen:
                    seen.add(Neigbhour)
                    visit.append(Neigbhour)

    def Depth_First_iterative(self,node,seen):
        seen.add(node)
        print(node)
        for Neigbhour in self.Graph[node]:
            if Neigbhour not in seen:
                seen.add(Neigbhour)
                self.Depth_First_iterative(Neigbhour,seen)
        
    def Breadth_First_Search(self,node):
        seen = set()
        visit = []
        visit.append(node)
        seen.add(node)
        while visit :
            curr = visit.pop(0)
            print(curr)
            for Neigbhour in self.Graph[curr]:
                if Neigbhour not in seen:
                    seen.add(Neigbhour)
                    visit.append(Neigbhour)









MyGraph = Graph()
MyGraph.add_edge("A","B")
MyGraph.add_edge("A","C")
MyGraph.add_edge("C","D")
MyGraph.add_edge("B","D")
MyGraph.add_edge("D","E")
MyGraph.add_edge("E","A")
MyGraph.display_graph()
seen = set()
# MyGraph.Depth_First_iterative("A",seen)
# MyGraph.Depth_First_Search()
MyGraph.Breadth_First_Search("A")

        



