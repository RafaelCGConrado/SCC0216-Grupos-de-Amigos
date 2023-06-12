#Terceiro trabalho da disciplina Modelagem Computacional em Grafos - ICMC USP 2023
#Aluno: Rafael C. G. Conrado

class Vertex:

    def __init__(self, key):
        self.key = key #Chave do vértice
        self.color = -1 #Cores: -1 branco, 0 cinza e 1 preto
        self.near = [] #Lista de adjacências de cada vértice
        self.time = 1 #Cada vértice possui um tempo de descoberta associado a DFS
        self.low = -1 #Inicia o low como -1
        self.isInStack = False #Verifica se o vértice está na pilha do algoritmo



class Graph:

    def __init__(self, nVertex, nEdges):
        self.vertexes = nVertex #Número de vértices do grafo
        self.edges = nEdges  #Número de arestas
        self.graph_ = []   #Lista de vértices do grafo
        self.time = 1      #Tempo 'global' do grafo (usado na DFS)
        self.nCfcs = 0     #Número de componentes fortemente conexos
        self.Cfcs = []     #Lista com os componentes fortemente conexos

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

    def DfsTarjan(self, v, stack):
        #Pinta o vértice de cinza (visitado)
        self.graph_[v].color = 0 
        
        #Salva o tempo de descoberta
        self.graph_[v].time = self.time
        
        #Define o low inicialmente como o tempo de descoberta
        self.graph_[v].low = self.time

        #Empilha o vértice na pilha do algoritmo de trajan
        self.graph_[v].isInStack = True
        stack.append(self.graph_[v])
        
        #Aumenta o tempo 'global' do grafo
        self.time += 1
        
        #Para cada vizinho do vértice atual:
        for neighbour in self.graph_[v].near:
            #Caso o vértice seja branco (não visitado)
            if self.graph_[neighbour].color == -1:
                self.DfsTarjan(neighbour, stack)

                #teste abaixo
                self.graph_[v].low = min(self.graph_[v].low, self.graph_[neighbour].low)

            #teste abaixo tambem
            elif(self.graph_[neighbour].isInStack == True):
                self.graph_[v].low = min(self.graph_[v].low, self.graph_[neighbour].time)


        #Algoritmo de Trajan utilizando a pilha:
        
        #Lista onde cada componente fortemente conexo será salvo:
        resultsList = []
        
        vertexKey = -1

        #Caso o low do vértice atual seja igual ao seu tempo de descoberta,
        #podemos dizer que ele é o 'head' de um CFC
        if(self.graph_[v].low == self.graph_[v].time):
            while(vertexKey != v):
                
                #Desempilha e adiciona na lista do CFS
                vertex = stack.pop()
                vertexKey = vertex.key
                resultsList.append(vertexKey)

                #Altera o status do vértice na pilha
                self.graph_[vertexKey].isInStack = False
            
            #Aumenta o número de componentes fortemente conexos do grafo
            self.nCfcs += 1
            resultsList.sort()
            self.Cfcs.append(resultsList)
        

    def printCfcs(self):
        self.Cfcs.sort()
        
        for list in self.Cfcs:
            for key in list:
                print(key, end = ' ')
            print()
    


    