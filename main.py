from graph import Graph, Vertex

#Leitura do número de vértices e de arestas
nVertexes, nEdges = map(int, input().split())

#Cria grafo
graph = Graph(nVertexes, nEdges)

#Leitura das conexões
for i in range(nEdges):
    source, destiny = map(int, input().split())
    graph.addEdge(source, destiny)

#Cria a pilha que será utilizada no algoritmo e chama o DFS
stack = []
for i in range(len(graph.graph_)):
    if graph.graph_[i].color == -1:
        graph.DfsTarjan(i, stack)

#Printa resultados
print(graph.nCfcs)
graph.printCfcs()