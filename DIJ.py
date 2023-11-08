from queue import PriorityQueue
from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        v, e = list(map(int, next(f).strip().split(' ')))
        edges = defaultdict(list)
        distances = defaultdict(lambda: float("INF"))
        data = list(map(lambda x: list(map(int, x.split(' '))), f.read().strip().split('\n')))
        pq = PriorityQueue()

        for a, b, w in data:
            edges[a].append((w, a, b))

        [pq.put(x) for x in edges[1]]
        distances[1] = 0
        while not pq.empty(): 
            w, a, b = pq.get()
            [pq.put(x) for x in edges[b]]

            if distances[a] + w < distances[b]:
                distances[b] = distances[a] + w
