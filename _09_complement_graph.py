def read_simple_graph(vertex_number, edge_number):
    graph = [[0] * vertex_number for i in range(vertex_number)]
    for j in range(edge_number):
        l1, l2 = map(int, input().split())
        graph[l1][l2] = 1
        graph[l2][l1] = 1
    return graph


def build_complement(graph):
    new = [[] for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 0:
                new[i].append(j)
    return new

v, e = list(map(int, input().split()))
my_graph = read_simple_graph(v, e)
my_graph = build_complement(my_graph)
print(my_graph)
