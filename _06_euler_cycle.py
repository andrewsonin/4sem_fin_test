from _03_adjacency_list import read_graph

def is_euler(graph):
    for v in graph:
        if len(v) % 2 == 1:
            return False
    return True

v, e = list(map(int, input().split()))
my_graph = read_graph(v, e)
if is_euler(my_graph):
    print('YES')
else:
    print('NO')
