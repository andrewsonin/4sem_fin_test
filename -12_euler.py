# def read_graph(vertex_number, edge_number):
#     graph = [[] for i in range(vertex_number)]
#     edges = []
#     for i in range(edge_number):
#         v1, v2 = map(int, input().split())
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#         edges.append((v1, v2))
#         edges.append((v2, v1))
#     return graph, edges
#
#
# def dfs(graph, vertex, used, path, edges):
#     path.append(vertex)
#     used.add(vertex)
#     for neighbour in graph[vertex]:
#         if len(path) == len(graph) and path[0] == neighbour:
#             return path
#         if (vertex, neighbour) in edges:
#             edges.pop(edges.index((vertex, neighbour)))
#             edges.pop(edges.index((neighbour, vertex)))
#             a = dfs(graph, neighbour, used, path, edges)
#             if a:
#                 return a
#             edges.append((vertex, neighbour))
#             edges.append((neighbour, vertex))
#     path.pop()
#
#
# def find_cycles(graph, edges, vertex=0):
#     cycles = []
#     path = []
#     used = set()
#     print(dfs(graph, vertex, used, path, edges))
#     print(cycles)
#
# v, e = map(int, input().split())
# my_graph, edges = read_graph(v, e)
# find_cycles(my_graph, edges)
