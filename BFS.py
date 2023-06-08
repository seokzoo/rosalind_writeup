from collections import defaultdict
from collections import deque

def BFS(edges, start, end):
    visited = []
    queue = deque()
    queue.append([start, 0]) 

    while len(queue) > 0:
        node, length = queue.popleft()
        if node == end:
            return length
        visited.append(node)
        for x in edges[node]:
            if x not in visited:
                queue.append([x, length+1])

    return -1

if __name__ == "__main__":
    with open("data") as f:
        splited = f.read().splitlines()
        edges = defaultdict(list)
        v, e = list(map(int, splited[0].split()))

        for x in splited[1:]:
            a, b = list(map(int, x.split()))
            edges[a].append(b)

        r = [BFS(edges, 1, node) for node in range(1, v+1)]
        print(" ".join(map(str, r)))
            
