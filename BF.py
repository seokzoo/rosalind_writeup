from collections import defaultdict

def conv(text_iter):
    for text_line in text_iter:
        yield list(map(int, text_line.split(' ')))

if __name__ == "__main__":
    with open("data") as f:
        v, e = map(int, next(f).strip().split(' '))
        graph = defaultdict(list)
        for a, b, w in conv(f.readlines()):
            graph[a].append((b, w))
        dist = [float('inf') for _ in range(v+1)]
        dist[1] = 0

        for _ in range(v+1):
            reached = [i for i, e in enumerate(dist) if e != float('inf')]
            for idx in reached:
                for b, w in graph[idx]:
                    if dist[b] > dist[idx] + w:
                        dist[b] = dist[idx] + w
        ans = []
        for e in dist[1:]:
            if e == float('inf'):
                ans.append('x')
            else:
                ans.append(str(e))
        print(' '.join(ans))
