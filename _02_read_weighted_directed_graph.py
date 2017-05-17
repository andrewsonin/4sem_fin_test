def read_wd_graph(edge_number):
    graph = {}
    for i in range(edge_number):
        v1, v2, w = list(map(str, input().split()))
        w = int(w)
        graph[v1] = [(v2, w)] + graph.get(v1, [])
    return graph

e = int(input())
my_graph = read_wd_graph(e)
print(my_graph)
