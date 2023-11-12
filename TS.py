from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        data = list(map(lambda x: list(map(int, x.split(' '))), f.read().strip().split('\n')))
        v, e = data[0]
        g = [[] for i in range(v+1)]
        rev = [[] for i in range(v+1)]
        solution = []
        for a, b in data[1:]:
            g[a].append(b)
            rev[b].append(a)
        while len(solution) != v:
            empty = []
            for i, e in enumerate(g[1:]):
                if not e:
                    empty.append(i+1)
            peek = list(set(empty) - set(solution))
            for e in peek:
                for x in rev[e]:
                    g[x].remove(e)
            solution += peek
        print(' '.join(map(str, solution[::-1])))
