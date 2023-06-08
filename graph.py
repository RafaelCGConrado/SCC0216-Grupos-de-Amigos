class Vertex:

    def __init__(self, key):
        self.key = key #Chave do vértice
        self.color = -1 #Cores: -1 branco, 0 cinza e 1 preto
        self.near = [] #Lista de adjacências de cada vértice
        self.time = 0 #Cada vértice possui um tempo de descoberta associado a DFS




class Graph:

    def __init__(self, nVertex, nEdges):
        self.vertexes = nVertex
        self.edges = nEdges
        self.graph_ = []
        

        #Inicializa o grafo com seus vértices
        for i in range(self.vertexes):
            newVertex = Vertex(i)
            self.graph_.append(newVertex)

    
    #Adiciona uma aresta entre dois vértices
    def addEdge(self, source, destiny):
        self.graph_[source].near.append(destiny)


    #Printa grafo (usada para testes)
    def printGraph(self):
        for i in range(self.vertexes):
            
            actualEdges = len(self.graph_[i].near)
            if actualEdges == 0:
                print(f'{i}')
            for j in range(actualEdges):
                print(f'{i} -> {self.graph_[i].near[j]}')


    def Dfs(self, v):
        self.graph_[v].color = 0  #Pinta o vértice de cinza
        print(v, end = ' ')

        for neighbour in self.graph_[v].near:
            if self.graph_[neighbour].color == -1: #Caso o vértice seja branco (não visitado)
                self.Dfs(neighbour)



    def DfsTarjan(self, v, pilha, discovery_time):
        self.graph_[v].color = 0  #Pinta o vértice de cinza
        
        #calcular e armazenar seu valor low
        self.graph_[v].time = discovery_time
        # pilha.append(self.graph_v[v])
        print(v, end = ' ')
        print(self.graph_[v].time)
        

        for neighbour in self.graph_[v].near:
            if self.graph_[neighbour].color == -1: #Caso o vértice seja branco (não visitado)
                self.DfsTarjan(neighbour, pilha, discovery_time+1)

