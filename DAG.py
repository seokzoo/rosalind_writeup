from collections import defaultdict
from copy import deepcopy

def hasCycle(g, visited, path, start):
    current = start
    visited.add(start)
    path.append(current)
    for adj in g[current]:
        if adj not in path:
            if hasCycle(g, visited, deepcopy(path), adj) == 1:
                return 1
        elif adj != current:
            return 1
    return 0

if __name__ == "__main__":
    with open("data") as f:
        data = f.read().strip().split("\n\n")
        n = data[0]
        solution = []
        for x in data[1:]:
            stack = []
            d = list(map(lambda x: list(map(int, x.split(' '))), (x.split('\n'))))
            v, e = d[0]
            g = defaultdict(list)
            visited = set()
            starts = set()
            for a, b in d[1:]:
                g[a].append(b)
                starts.add(a)
            found = False
            while starts:
                if hasCycle(g, visited, [], starts.pop()):
                    found = True
                    break
                starts -= visited
            if found == True:
                solution.append("-1")
            else:
                solution.append("1")

        print(' '.join(solution))
