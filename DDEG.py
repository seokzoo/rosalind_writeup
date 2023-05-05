from collections import defaultdict

data = open("data").read().splitlines()

graph = defaultdict(list)

for x in data[1:]:
    a, b = list(map(int, x.split(' ')))
    graph[a].append(b)
    graph[b].append(a)

n = int(data[0].split(' ')[0])

ans = []
for i in range(1, n+1):
    ans.append(sum([len(graph[x]) for x in graph[i]]))
    

print(' '.join(list(map(str, ans))))
