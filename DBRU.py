from rosalind.rosalind import get_rc

if __name__ == "__main__":
    with open("data") as f:
        data = list(map(lambda x: x.strip(), f.read().strip().split('\n')))
        n = len(data[0])
        data += [get_rc(seq) for seq in data]
        data = list(set(data))
        for x in data:
            print(f"({x[:n-1]}, {x[-n+1:]})")
