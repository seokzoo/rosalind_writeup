if __name__ == "__main__":
    with open("data") as f:
        data = f.read().strip().split('\n')

        n = len(data)
        size = len(data[0])

        tree = [{} for i in range(size)]
        data_dict = {x: i for i, x in enumerate(data)}
        for seq in data:
            for i, c in enumerate(seq):
                if c not in tree[i]:
                    tree[i][c] = []
                tree[i][c].append(seq)
        for pos in tree:
            solution = [0 for i in range(n)]
            subsize = len(pos[list(pos)[0]])
            if 1 < subsize and subsize < n - 1:
                for seq in pos[list(pos)[0]]:
                    solution[data_dict[seq]] = 1
                print(''.join(map(str, solution)))
