from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        splited = f.read().strip().split('\n\n')[1:]

        for data in splited:
            vdata = data.split('\n')
            v, e = map(int, vdata[0].split(' '))
            graph = defaultdict(list)
            rev = defaultdict(list)
            inner = set()
            for verties in vdata[1:]:
                a, b = map(int, verties.split(' '))
                graph[a].append(b) 
                rev[b].append(a)
                inner.add(a)
            u = set([i for i in range(1, v+1)])
            solution = [] 
            found = True
            for _ in range(v):
                outter = list(u - inner - set(solution))
                if len(outter) != 1:
                    found = False
                    print('-1')
                    break
                solution.append(outter[0])
                for v in rev[outter[0]]:
                    graph[v].remove(outter[0])
                    if not graph[v]:
                        inner.discard(v)
                    
            if found == True:
                print('1 ' + ' '.join(map(str, solution[::-1])))
