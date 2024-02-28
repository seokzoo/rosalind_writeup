from queue import PriorityQueue
from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        
        graphs = []
        data = list(map(lambda x: list(map(int, x.split(' '))), f.read().strip().split('\n')[1:]))
        idx = 0 
        while idx < len(data):
            graphs.append(data[idx:data[idx][1]+idx+1])
            idx += (data[idx][1]+1)
        solution = []
        for splited in graphs:
            v, e = splited[0]
            g = defaultdict(list)
            given = splited[1]
            pq = PriorityQueue()
            distances = defaultdict(lambda: float("INF"))
            for a, b, w in splited[1:]:
                g[a].append((b, w))
            distances[given[1]] = 0
            pq.put((given[1], 0))
            while not pq.empty(): 
                b, w = pq.get()
                for nb, nw in g[b]:
                    if distances[b] + nw < distances[nb]:
                        distances[nb] = distances[b] + nw
                        pq.put((nb, nw))
            if given[0] in distances:
                solution.append(str(distances[given[0]] + given[2]))
            else:
                solution.append('-1')
        print(' '.join(solution))
