from collections import defaultdict
from collections import deque

if __name__ == "__main__":
    edges = defaultdict(lambda : [])
    splited = open("data").read().splitlines()
    n = int(splited[0])

    for x in splited[1:]:
        a, b = list(map(int, x.split(' ')))
        edges[a].append(b)
        edges[b].append(a)

    queue = deque()
    count = 0
    unvisited = [i for i in range(1, n+1)]
    while len(unvisited) > 0:
        count += 1
        queue.append(unvisited[0])
        visited = []
        while len(queue) > 0:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                unvisited.remove(node)
                queue += edges[node]
    print(count-1)
