def read_graph(edge_number):
    graph = []
    for i in range(edge_number):
        graph.append(tuple(map(int, input().split())))
    return graph


def kruscal(graph, num_of_vertexes):
    edges = sorted(graph, key=lambda x: x[2])
    names_of_components = [i for i in range(num_of_vertexes)]
    tree = []
    tree_weight = 0
    for v1, v2, cost in edges:
        previous_comp = names_of_components[v1]
        if names_of_components[v1] != names_of_components[v2]:
            tree.append((v1, v2))
            tree_weight += cost
            for i in range(num_of_vertexes):
                if names_of_components[i] == previous_comp:
                    names_of_components[i] = names_of_components[v1]
    return tree_weight, tree

v, e = map(int, input().split())
a = kruscal(read_graph(e), v)
print(a[1])
for elem in a[0]:
    print(*elem)
