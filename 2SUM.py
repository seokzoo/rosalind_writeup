from itertools import product

if __name__ == "__main__":
    with open("data") as f:
        data = list(map(lambda x: x.strip(), f.read().strip().split('\n')))
        data = [list(map(int, x.split(' '))) for x in data]
        data = data[1:]
        for x in data:
            sorted_l = sorted([(e, i) for i, e in enumerate(x)])
            left = [(-e[0], e[1]) for e in sorted_l if e[0] < 0]
            right = [e for e in sorted_l if e[0] >= 0][::-1]
            u = list(set([e[0] for e in left]) & set([e[0] for e in right]))

            if not u:
                zero = [e for e in right if e[0] == 0]
                if len(zero) >= 2:
                    print(f'{zero[-1][1] + 1} {zero[-2][1] + 1}')
                else:
                    print(-1)
                continue
            else:
                comm = u[0]
                a = [e[1]+1 for e in left if e[0] == comm]
                b = [e[1]+1 for e in right if e[0] == comm]
                e = list(product(a, b))[0]
                print('{} {}'.format(min(e), max(e)))
