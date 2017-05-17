def read_graph(edge_number):
    graph = {}
    for i in range(edge_number):
        v1, v2 = map(str, input().split())
        graph[v1] = graph.get(v1, []) + [v2]
    return graph


def bfs(graph, start, end):
    queue = [start]
    while queue:
        cur = queue.pop(0)
        for neighbour in graph.get(cur, []):
            if neighbour == end:
                return True
            queue.append(neighbour)
    return False

vx1, vx2 = map(str, input().split())
my_graph = read_graph(int(input()))
if bfs(my_graph, vx1, vx2) or bfs(my_graph, vx2, vx1):
    print('YES')
else:
    print('No descendants')
