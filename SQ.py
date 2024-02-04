from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        splited = f.read().split('\n\n')[1:]
        ans = []

        for data in splited:
            graph = defaultdict(set)

            splited = data.split('\n')
            v, _ = list(map(int, splited[0].split(' ')))
            for edges in splited[1:]:
                if edges == '':
                    continue
                a, b = list(map(int, edges.split(' ')))
                graph[a].add(b)
                graph[b].add(a)

            depth = 4
            unvisited = [i for i in range(1, v+1)]
            found = False

            while unvisited:
                start = unvisited.pop()
                queue = [[start]]
                for _ in range(depth):
                    new = []
                    while queue:
                        path = queue.pop()
                        for node in graph[path[-1]]:
                            if len(path) >= 2:
                                if node == path[-2]:
                                    continue
                            new.append(path + [node])
                    queue = new
                if any([path[0] == path[-1] for path in queue]):
                    found = True
                    ans.append(1)
                    break
                connected_nodes = graph[start]
                for node in connected_nodes:
                    graph[node].remove(start)
            if found == False:
                ans.append(-1)

        print(' '.join(map(str, ans)))
