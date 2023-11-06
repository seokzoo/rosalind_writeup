
def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    l, r = [], []
    for e in arr[1:]:
        if e <= pivot:
            l.append(e)
        else:
            r.append(e)
    return qsort(l) + [pivot] + qsort(r)

if __name__ == "__main__":
    with open("data") as f: 
        n = int(next(f))
        arr = list(map(int, next(f).strip().split(' ')))

        print(' '.join(map(str, qsort(arr))))
