def read_simple_graph(vertex_number, edge_number):
    graph = [[0] * vertex_number for i in range(vertex_number)]
    for j in range(edge_number):
        l1, l2 = map(int, input().split())
        graph[l1][l2] = 1
        graph[l2][l1] = 1
    return graph
