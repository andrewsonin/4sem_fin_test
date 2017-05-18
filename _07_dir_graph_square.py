def read_graph(vertex_number, edge_number):
    graph = [[] for i in range(vertex_number)]
    for i in range(edge_number):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
    return graph


def squarify(graph):
    len_gr = len(graph)
    sq_graph = [[0] * len_gr for i in range(len_gr)]
    for start in range(len_gr):
        used = {start}
        queue = [(start, 0)]
        sq_graph[start][start] = 1
        while queue:
            cur, time = queue.pop(0)
            if time == 2:
                break
            time += 1
            for neighbour in graph[cur]:
                if neighbour not in used:
                    sq_graph[start][neighbour] = 1
                    queue.append((neighbour, time))
    return sq_graph

v, e = map(int, input().split())
my_graph = read_graph(v, e)
my_graph = squarify(my_graph)
for v in my_graph:
    print(' '.join(map(str, v)))
