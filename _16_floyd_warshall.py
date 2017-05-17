def read_graph(vertex_number, edge_number):
    graph = [[float('+inf')] * vertex_number for i in range(vertex_number)]
    for i in range(edge_number):
        v1, v2, w = map(int, input().split())
        graph[v1][v2] = w
        if i < vertex_number:
            graph[i][i] = 0
    return graph


def floyd_warshall(graph):
    n = len(graph)
    w = graph.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                w[i][j] = min(w[i][j], w[i][k] + w[k][j])
    return w

v, e = map(int, input().split())
my_graph = read_graph(v, e)
for string in floyd_warshall(my_graph):
    print(' '.join(map(str, string)))
