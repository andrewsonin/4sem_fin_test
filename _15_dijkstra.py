def read_graph(edge_number):
    graph = {}
    for i in range(edge_number):
        v1, v2, w = map(str, input().split())
        w = int(w)
        graph[v1] = [(v2, w)] + graph.get(v1, [])
    return graph


def dijkstra(graph, start=None):
    from heapq import heappush, heappop
    if not graph:
        return {}
    if start is None:
        start, val = graph.popitem()
        graph[start] = val
    paths = {start: (0, [start])}
    path_heap = []
    heappush(path_heap, (0, start))
    while path_heap:
        cur = heappop(path_heap)[1]
        for neighbour in graph.get(cur, []):
            length = paths[cur][0] + neighbour[1]
            if length < paths.get(neighbour[0], [float('+inf')])[0]:
                paths[neighbour[0]] = (length, paths[cur][1] + [neighbour[0]])
                heappush(path_heap, (length, neighbour[0]))
    return paths

e = int(input())
my_graph = read_graph(e)
print(dijkstra(my_graph, '2'))
