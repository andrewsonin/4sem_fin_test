def read_graph(vertex_number, edge_number):
    graph = [[] for i in range(vertex_number)]
    reversed_graph = [[] for i in range(vertex_number)]
    for i in range(edge_number):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        reversed_graph[v2].append(v1)
    return graph, reversed_graph


def dfs(vertex, graph, used, stack):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used, stack)
    stack.append(vertex)


def kosaraju(graph, reversed_graph):
    stack = []
    used = set()
    for i in range(len(graph)):
        if i not in used:
            dfs(i, graph, used, stack)
    used = set()
    components = []
    for i in range(-1, -len(graph) - 1, -1):
        if stack[i] not in used:
            print(used)
            addition = []
            dfs(stack[i], reversed_graph, used, addition)
            components.append(addition)
    return components


n, m = map(int, input().split())
my_graph, rev_graph = read_graph(n, m)
print(kosaraju(my_graph, rev_graph))
