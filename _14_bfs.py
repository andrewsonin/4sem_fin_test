def read_graph(vertex_number, edge_number):
    graph = [[0] * vertex_number for i in range(vertex_number)]
    for j in range(edge_number):
        l1, l2 = map(int, input().split())
        graph[l1][l2] = 1
        graph[l2][l1] = 1
    return graph


def find_comps(graph):
    len_gr = len(graph)
    non_used = {i for i in range(len_gr)}
    comps = []
    while non_used:
        addition = []
        start = non_used.pop()
        queue = [(start, 0)]
        while queue:
            cur, time = queue.pop(0)
            non_used.discard(cur)
            addition.append((cur, time))
            for i in range(len_gr):
                if graph[cur][i] == 1 and i in non_used:
                    non_used.remove(i)
                    queue.append((i, time + 1))
        comps.append(addition)
    return comps

v, e = map(int, input().split())
my_graph = read_graph(v, e)
print(find_comps(my_graph))
