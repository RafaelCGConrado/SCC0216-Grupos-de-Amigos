from graph import Graph, Vertex

#Leitura do número de vértices e de arestas
nVertexes, nEdges = map(int, input().split())

#Cria grafo
graph = Graph(nVertexes, nEdges)

#Leitura das conexões
for i in range(nEdges):
    source, destiny = map(int, input().split())
    graph.addEdge(source, destiny)

#Printa grafo construído
graph.printGraph()