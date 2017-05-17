def read_simple_graph(vertex_number, edge_number):
    graph = [[0] * vertex_number for i in range(vertex_number)]
    for j in range(edge_number):
        l1, l2 = list(map(int, input().split()))
        graph[l1][l2] = 1
    return graph

v, e = list(map(int, input().split()))
my_graph = read_simple_graph(v, e)
for i in range(v):
    out_power = sum(my_graph[i])
    in_power = 0
    for j in range(v):
        in_power += my_graph[j][i]
    print(i, in_power, out_power)
