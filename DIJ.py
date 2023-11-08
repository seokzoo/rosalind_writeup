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

        distances[1] = 0
        pq.put((0, 0, 1))
        while not pq.empty(): 
            w, a, b = pq.get()
            for nw, na, nb in edges[b]:
                if distances[b] + nw < distances[nb]:
                    distances[nb] = distances[b] + nw
                    pq.put((nw, na, nb))
        solution = []
        for i in range(1, v+1):
            if distances[i] == float("INF"):
                solution.append("-1") 
            else:
                solution.append(str(distances[i]))
        print(' '.join(solution))
