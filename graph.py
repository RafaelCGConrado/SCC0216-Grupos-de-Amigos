class Vertex:

    def __init__(self, key):
        self.key = key #Chave do vértice
        self.color = -1 #Cores: -1 branco, 0 cinza e 1 preto
        self.near = [] #Lista de adjacências de cada vértice




class Graph:

    def __init__(self, nVertex, nEdges):
        self.vertexes = nVertex
        self.edges = nEdges
        self.graph_ = []

        #Inicializa o grafo com seus vértices
        for i in range(self.vertexes):
            newVertex = Vertex(i)
            self.graph_.append(newVertex)

        
    def addEdge(self, source, destiny):
        self.graph_[source].near.append(destiny)


    def printGraph(self):
        for i in range(self.vertexes):
            
            actualEdges = len(self.graph_[i].near)
            for j in range(actualEdges):
                print(f'{i} -> {self.graph_[i].near[j]}')
                print()