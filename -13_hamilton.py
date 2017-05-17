def read_graph(vtx, edg):
    matrix = [[float('+inf')] * vtx for i in range(vtx)]
    graph = [[] for i in range(vtx)]
    for i in range(edg):
        v1, v2, w = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
        matrix[v1][v2] = matrix[v2][v1] = w
    return graph, matrix


def find_h(graph, matrix, graph_len, cycles, cur_weight=0, vertex=0, used=set(), path=list()):
    used.add(vertex)
    path.append(vertex)
    if len(path) == graph_len and path[0] in graph[path[-1]]:
        cycles.append([path.copy(), cur_weight + matrix[path[-1]][path[0]]])
    else:
        for neighbour in graph[vertex]:
            if neighbour not in used:
                find_h(graph, matrix, graph_len, cycles, cur_weight + matrix[vertex][neighbour], neighbour, used, path)
    path.pop()
    used.remove(vertex)

vertexes, edges = map(int, input().split())
graph, weight_matrix = read_graph(vertexes, edges)
cycles_list = []
find_h(graph, weight_matrix, vertexes, cycles_list)
print(cycles_list)
