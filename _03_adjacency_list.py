def read_graph(vertex_number, edge_number):
    graph = [[] for i in range(vertex_number)]
    for i in range(edge_number):
        v1, v2 = list(map(int, input().split()))
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph
