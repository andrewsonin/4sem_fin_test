def read_graph(vertex_number, edge_number):
    graph = [[] for i in range(vertex_number)]
    for i in range(edge_number):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
    return graph


def is_path_between(graph, start, end):
    if start == end:
        return True
    used = {start}
    queue = [start]
    while queue:
        cur = queue.pop(0)
        for neighbour in graph[cur]:
            if neighbour not in used:
                if neighbour == end:
                    return True
                queue.append(neighbour)
                used.add(neighbour)
    return False

v, e = map(int, input().split())
my_graph = read_graph(v, e)
m = int(input())
answers = []
for i in range(m):
    st, en = map(int, input().split())
    if is_path_between(my_graph, st, en):
        answers.append('YES')
    else:
        answers.append('NO')
print(' '.join(map(str, answers)))
