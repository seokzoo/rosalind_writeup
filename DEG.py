from collections import defaultdict

data = open("data").read().splitlines()

graph = defaultdict(list)

for x in data[1:]:
    a, b = list(map(int, x.split(' ')))
    graph[a].append(b)
    graph[b].append(a)

print(' '.join([str(len(graph[x])) for x in range(1, int(data[0].split(' ')[0])+1)]))
