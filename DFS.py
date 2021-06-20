class Graph:
    def __init__(self, gdict=None):
        self.gdict = gdict
    def addconnection(self, vertex, edge):
        self.gdict[vertex].append(edge)
    def countconnection(self,node):
        return len(self.gdict[node])
    def addNode(self,newnode):
        self.gdict[newnode] = []
    # traversal
    def showNode(self):
        return self.gdict.keys()
    def showValues(self):
        return self.gdict.values()
    def bfs(self,vertex):
        if vertex not in self.gdict:
            print("not found :",vertex, "in", self.gdict.keys())
        else:
            queue = [ vertex ]
            visited = [ vertex ]
            while queue:
                deVertex = queue.pop(0)
                print(deVertex)
                for adjacentVertex in self.gdict[deVertex]:
                    if adjacentVertex not in visited:
                        # add into stack
                        queue.append(adjacentVertex)
                        # mark it visited
                        visited.append(adjacentVertex)
    def dfs(self,vertex):
        if vertex not in self.gdict:
            print("not found :",vertex, "in", self.gdict.keys())
        else:
            stack = [ vertex ]
            visited = [ vertex ]
            while stack:
                popVertex = stack.pop()
                print(popVertex)
                for adjacentVertex in self.gdict[popVertex]:
                    if adjacentVertex not in visited:
                        # enqueue add into queue
                        stack.append(adjacentVertex)
                        # mark it visited
                        visited.append(adjacentVertex)
