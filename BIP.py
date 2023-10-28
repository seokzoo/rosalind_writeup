from collections import defaultdict, deque

if __name__ == "__main__":
    with open("data") as f:
        n = int(next(f))
        data = list(map(lambda x: list(map(lambda x: tuple(map(int, x.split(' '))), x.split('\n'))), f.read().strip().split("\n\n")))
        solution = []

        for x in data:
            graph = defaultdict(list)
            v, e = x[0]
            s1, s2 = [], []
            for a, b in x[1:]:
                graph[a].append(b)
                graph[b].append(a)
            q = deque()
            unvisited = set([i for i in range(1, v+1)])
            q.append(1)
            s1.append(1)
            found = False
            while len(unvisited) > 0:
                if len(q) == 0:
                    q.append(list(unvisited)[0])
                current = q.pop()
                if current in s1:
                    if sum([(v in s1) for v in graph[current]]) != 0:
                        found = True
                    s2 += list(set(graph[current])-set(s2))
                elif current in s2:
                    if sum([(v in s2) for v in graph[current]]) != 0:
                        found = True
                    s1 += list(set(graph[current])-set(s1))
                unvisited.discard(current)
                q += list(set(graph[current]) & unvisited)
                if found:
                    break
            if found == True:
                solution.append('-1')
            else:
                solution.append('1')
        print(' '.join(solution))
