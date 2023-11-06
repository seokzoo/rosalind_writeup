
if __name__ == "__main__":
    with open("data") as f:
        n = int(next(f))
        arr = list(map(int, next(f).strip().split(' ')))
        k = int(next(f))
        
        l, v, r = [], [], []
        prev = 0
        while True:
            if len(arr) == 1:
                print(arr[0])
                break
            v.append(arr[0])
            for e in arr[1:]:
                if e < v[0]:
                    l.append(e)
                elif e == v[0]:
                    v.append(e)
                else:
                    r.append(e)
            if k >= len(l) + 1 and k <= len(l) + len(v):
                print(v[0])
                break
            elif k <= len(l):
                arr = l
                l, v, r = [], [], []
            elif k > len(v) + len(l):
                arr = r
                k = k - (len(v) + len(l))
                l, v, r = [], [], []
