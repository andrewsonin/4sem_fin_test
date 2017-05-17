def read_graph(vertex_number, edge_number):
    graph = [[] for i in range(vertex_number)]
    for i in range(edge_number):
        v1, v2 = list(map(int, input().split()))
        graph[v1].append(v2)
    return graph

def transpose(graph):
    tr_graph = [[] for i in range(len(graph))]
    for i in range(len(graph)):
        for edge in graph[i]:
            tr_graph[edge].append(i)
    return tr_graph

v, e = list(map(int, input().split()))
my_graph = read_graph(v, e)
my_graph = transpose(my_graph)
print(my_graph)
