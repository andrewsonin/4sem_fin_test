def read_graph(vertex_number, edge_number):
    graph = [[0] * vertex_number for i in range(vertex_number)]
    for j in range(edge_number):
        l1, l2 = map(int, input().split())
        graph[l1][l2] = 1
        graph[l2][l1] = 1
    return graph


def find_con_comps(graph):
    def local_dfs(graph, start, addition, non_used):
        non_used.discard(start)
        addition.append(start)
        for j in range(len(graph)):
            if graph[start][j] == 1 and j in non_used:
                local_dfs(graph, j, addition, non_used)

    non_used = {i for i in range(len(graph))}
    comps = []
    while non_used:
        start = non_used.pop()
        addition = []
        local_dfs(graph, start, addition, non_used)
        comps.append(addition)
    return comps

v, e = map(int, input().split())
my_graph = read_graph(v, e)
print(find_con_comps(my_graph))
