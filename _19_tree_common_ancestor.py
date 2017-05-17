def read_reversed_graph(edge_number):
    graph = {}
    for i in range(edge_number):
        v1, v2 = map(str, input().split())
        graph[v2] = graph.get(v2, []) + [v1]
    return graph


def define_ancestor(tree, v1, v2):
    q1 = [v1]
    q2 = [v2]
    while q1[-1] != q2[-1]:
        if tree.get(q1[-1], []):
            q1.append(tree.get(q1[-1], [])[0])
        if tree.get(q2[-1], []):
            q2.append(tree.get(q2[-1], [])[0])
    for i in range(-1, -min(len(q1), len(q2)) -1, -1):
        if q1[i] != q2[i]:
            return q1[i + 1]

vx1, vx2 = map(str, input().split())
my_graph = read_reversed_graph(int(input()))
print(define_ancestor(my_graph, vx1, vx2))
