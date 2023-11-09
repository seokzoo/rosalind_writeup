from rosalind.rosalind import get_rc

if __name__ == "__main__":
    with open("data") as f:
        data = list(map(lambda x: x.strip(), f.read().strip().split('\n')))
        n = len(data[0])
        size = len(data)
        DEBR = []
        for x in data:
            DEBR.append((x[:n-1], x[-n+1:]))

        thr = list(DEBR.pop())
        while DEBR:
            for i, x in enumerate(DEBR):
                if x[0] == thr[-1]:
                    thr.append(x[1])
                    del DEBR[i]
                    break
        print(''.join([thr[0]] + [x[-1] for x in thr[1:]])[:size])
