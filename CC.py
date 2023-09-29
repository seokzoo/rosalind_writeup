from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        data = list(map(lambda x : x.strip(), f.readlines()))
        n, e = list(map(int, data[0].split(' ')))
        g = defaultdict(list)

        count = 0
        not_visited = set([i for i in range(1, n+1)])
        stack = []
        for x in data[1:]:
            a, b = list(map(int, x.split(' ')))
            g[a].append(b)
            g[b].append(a)

        while not_visited:
            if not stack:
                count += 1
                stack.append(not_visited.pop())
            current = stack.pop()
            for x in g[current]:
                if x in not_visited:
                    stack.append(x)
                not_visited.discard(x)

        print(count)
