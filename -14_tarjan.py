def read_graph_as_lists(vertex_quantity, edge_quantity):
    graph = [[] for i in range(vertex_quantity)]
    for edge in range(edge_quantity):
        link1, link2 = map(int, input().split())
        graph[link1].append(link2)
    return graph


def topological_sorting(graph, vtx):
    non_used = {i for i in range(vtx)}
    path = []
    while non_used:
        cur = non_used.pop()
        dfs_tarjan(graph, cur, set(), non_used, path)
    return ' '.join(map(str, path[::-1]))


def dfs_tarjan(graph, vertex, grays=None, non_used=None, path=None):
    grays.add(vertex)
    non_used.discard(vertex)
    for neighbour in graph[vertex]:
        if neighbour in non_used:
            dfs_tarjan(graph, neighbour, grays, non_used, path)
        elif neighbour in grays:
            print('Sorting is impossible. The graph has a cycle.')
            exit(0)
    grays.remove(vertex)
    path.append(vertex)

vertex_number, edge_number = map(int, input().split())
print(topological_sorting(read_graph_as_lists(vertex_number, edge_number), vertex_number))
