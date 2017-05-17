def read_graph(vertex_number, edge_number):
    graph = [[] for i in range(vertex_number)]
    for i in range(edge_number):
        v1, v2, w = map(int, input().split())
        graph[v1].append((v2, w))
        graph[v2].append((v1, w))
    return graph


def prim(graph):
    spanning_vertexes = {0}
    tree = []
    for i in range(len(graph) - 1):
        min_length = float('+inf')
        for vertex in spanning_vertexes:
            for neighbour, weight in graph[vertex]:
                if neighbour not in spanning_vertexes and weight < min_length:
                    cur_v, cur_e, min_length = neighbour, (vertex, neighbour), weight
        spanning_vertexes.add(cur_v)
        tree.append(cur_e)
    return tree

vertex_number, edge_number = tuple(map(int, input().split()))
result = prim(read_graph(vertex_number, edge_number))
print(result)
