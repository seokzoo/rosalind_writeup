
if __name__ == "__main__":
    splited = open("data").read().splitlines()
    seq = list(map(int, splited[1].split()))
    pivot = seq[0]

    smaller = []
    bigger = []
    for x in seq[1:]:
        if x > pivot:
            bigger.append(x)
        else:
            smaller.append(x)
    permuted = smaller + [pivot] + bigger
    print(' '.join(list(map(str, permuted))))
