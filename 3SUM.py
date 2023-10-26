from itertools import combinations

if __name__ == "__main__":
    with open("data") as f:
        data = list(map(lambda x: x.strip(), f.read().strip().split('\n')))
        data = [list(map(int, x.split(' '))) for x in data]
        data = data[1:]
         
        for x in data:
            x = sorted([(n, i+1) for i, n in enumerate(x)])
            l = [e for e in x if e[0] < 0] 
            p = [e for e in x if e[0] >= 0] 
            zeros = sorted([e[1] for e in x if e[0] == 0])
            # three zeros
            if len(zeros) == 3:
                print(f'{zeros[0]} {zeros[1]} {zeros[2]}')
                continue
            # two negs
            comb = list(combinations(l, 2))
            m = max(p)[0]
            comb = ([e for e in comb if -sum([k[0] for k in e]) <= m])
            if comb:
                r = ''
                comm = set([-sum([e[0] for e in c]) for c in comb]) & set([e[0] for e in p])
                if comm:
                    comb = ([c for c in comb if -sum([e[0] for e in c]) in comm])
                    for c in comb:
                        s = -sum([e[0] for e in c])
                        for a in p:
                            if s == a[0]:
                                r = ' '.join(map(str, sorted([e[1] for e in c] + [a[1]])))
                                break
                        if r != '':
                            break
                    if r != '':
                        print(r)
                        continue
            # one negs
            solution = []
            possible = [e for e in p if e[0]]
            if len(possible) <= 1:
                break
            comb = list(combinations(possible, 2))
            comm = set([sum([e[0] for e in c]) for c in comb]) & set([-e[0] for e in l])
            if comm:
                comb = ([c for c in comb if sum([e[0] for e in c]) in comm])
                for c in comb:
                    s = sum([e[0] for e in c])
                    if solution:
                        break
                    for neg in l:
                        if s == -neg[0]:
                            solution += [(neg)]
                            solution += c
                            break
            if not solution:
                print(-1)
            else:
                print(' '.join(map(str, sorted([e[1] for e in solution]))))
