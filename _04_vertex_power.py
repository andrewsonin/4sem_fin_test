from _01_read_simple_graph import read_simple_graph

v, e = list(map(int, input().split()))
my_graph = read_simple_graph(v, e)

for i in range(v):
    print(i, sum(my_graph[i]))
