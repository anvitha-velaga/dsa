class graph:
    def __init__(self):
        self.graph={}
    def add_node(self,node):
        if node not in self.graph:
            self.graph[node]=[]
        else:
            print("node already present")
    def add_edge(self,p,q,directed=True):
        self.add_node(p)
        self.add_node(q)
        self.graph[p].append(q)
        if not directed:
            self.graph[q].append(p)
    def display(self):
        for node in self.graph:
            print(f"{node}->{self.graph[node]}")
g=graph()
g.add_edge('h','c')
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.display()