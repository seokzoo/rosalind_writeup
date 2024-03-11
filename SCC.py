from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        g = defaultdict(list)
        rev = defaultdict(list)
        v, e = map(int, f.readline().split(' '))
        for a, b in (list(map(int, line.split(' '))) for line in f.read().strip().split('\n')):
            g[a].append(b)
            rev[b].append(a)
        u = set([i for i in range(1, v+1)])
        visited = set()
        path = [] 
        stack = [1]
        while u-visited or stack:
            if not stack:
                stack.append(list(u-visited)[0])
            un = set(g[stack[-1]]) - visited
            visited.add(stack[-1])
            if not un:
                path.append(stack.pop())
            else: 
                stack += [list(un)[0]]
        
        cnt = 0
        stack = []
        visited = set()
        while u-visited or stack:
            if not stack:
                cnt += 1
                x = path.pop()
                while x in visited: 
                    x = path.pop()
                stack.append(x)
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            un = set(rev[current]) - visited
            stack += list(un)
        print(cnt)
