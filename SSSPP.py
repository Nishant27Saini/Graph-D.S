#algorithm
def my_dijkstra_algo(graph, initial):
    visited= { initial: 0 }
    path = defaultdict(list)
    
    nodes = set(graph.nodes)
# TIME COMPLEXITY O(V^2)
# NODES = VERTEX == v

#space complexity O(E)
# Edges == E
    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    
                    minNode = node
            
        if minNode is None:
             break
                
        nodes.remove(minNode)
        currentWeight = visited[minNode]
            
        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.weights[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    return visited, path
  
  
  
#Weighted Graph
from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.weights = {}
    
    def addNode(self, value):
        self.nodes.add(value)
        
    def addEdge(self, fromcity, tocity, cost):
        self.edges[fromcity].append(tocity)
        self.weights[(fromcity, tocity)] = cost
        
        
g  = Graph()
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addNode("F")
g.addNode("G")
g.addEdge("A", "B", 2)
g.addEdge("A", "C", 5)
g.addEdge("B", "C", 6)
g.addEdge("B", "E", 3)
g.addEdge("B", "D", 1)
g.addEdge("E", "G", 9)
g.addEdge("C", "F", 8)
g.addEdge("F", "G", 7)


#Algorithm Implementation on Weighted Graph
my_dijkstra_algo(g, "A")
