
count = 0

with open("data") as f:
    data = f.readlines()
    data = list(map(int, data[1].split(' ')))

    sorted_data = sorted(data, reverse=True)

    for x in sorted_data:
        idx = [i for i, e in enumerate(data) if e == x]
        count += sum([len(data) - e - 1 for e in idx])
        n = len(idx)
        count -= (n-1)*n/2
        for e in sorted(idx, reverse=True):
            del data[e]

    print(count)
