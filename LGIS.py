from collections import defaultdict

if __name__ == "__main__":
    splited = open("data").read().splitlines() 
    arr = list(map(int, splited[1].split()))
    size = int(splited[0])

    grid = defaultdict(lambda : [[0,[]] for _ in range(size)])
    grid2 = defaultdict(lambda : [[0,[]] for _ in range(size)])

    sorted_arr = sorted(arr)
    table = defaultdict(lambda : 0)
    for x in arr:
        table[x] = sorted_arr.index(x)

    changed = []
    changed2 = []
    for i in range(size):
        if i > 2:
            grid.pop(i-3)
            grid2.pop(i-3)
        if i == 0:
            grid[i][table[arr[i]]] = 1, [arr[i]]
            grid2[i][table[arr[i]]] = 1, [arr[i]]
            changed.append(table[arr[i]])
            changed2.append(table[arr[i]])
        else:
            k = table[arr[i]]
            longest = 0, []
            longest2 = 0, []
            for j in range(k, size):
                if longest[0] < grid[i-1][j][0]:
                    longest = grid[i-1][j]
            for j in range(k):
                if longest2[0] < grid2[i-1][j][0]:
                    longest2 = grid2[i-1][j]
            grid[i][k][0] = 1 + longest[0]
            grid[i][k][1] = longest[1] + [arr[i]]
            grid2[i][k][0] = 1 + longest2[0]
            grid2[i][k][1] = longest2[1] + [arr[i]]
            for x in changed:
                grid[i][x] = grid[i-1][x]
            for x in changed2:
                grid2[i][x] = grid2[i-1][x]
            changed.append(table[arr[i]])
            changed2.append(table[arr[i]])

    longest = [0, 0]
    for i, x in enumerate(grid2[size-1]):
        if longest[0] < x[0]:
            longest = x[0], i
    print(" ".join(list(map(str, (grid2[size-1][longest[1]][1])))))

    longest = [0, 0]
    for i, x in enumerate(grid[size-1]):
        if longest[0] < x[0]:
            longest = x[0], i
    print(" ".join(list(map(str, (grid[size-1][longest[1]][1])))))
