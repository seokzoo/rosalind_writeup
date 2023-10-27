from collections import defaultdict
from itertools import combinations

stoi = lambda x: list(map(int, x.split(' ')))

if __name__ == "__main__":
    with open("data") as f:
        solution = []
        data = list(map(lambda x: x.split('\n'), f.read().strip().split('\n\n')))
        length = 10
        pairs = []
        for x in data:
            pairs.append([stoi(x[0]), stoi(x[1])])
        for pair in pairs:
            possible = []
            visited = defaultdict(lambda: False)
            ranges = list(combinations([i for i in range(length)], 2))
            found = False
            if pair[0] == pair[1]:
                solution.append('0')
                continue
            for l, r in ranges:
                reversed_pair = pair[0][:l] + pair[0][l:r+1][::-1] + pair[0][r+1:]
                if reversed_pair == pair[1]:
                    solution.append('1')
                    found = True
                    break
                visited[str(reversed_pair)] = True
                possible.append(reversed_pair)
            if found:
                continue
            for i in range(2, 6):
                temp = []
                for x in possible:
                    for l, r in ranges:
                        reversed_pair = x[:l] + x[l:r+1][::-1] + x[r+1:]
                        if reversed_pair == pair[1]:
                            solution.append(str(i))
                            found = True
                            break
                        if visited[str(reversed_pair)] == False:
                            temp.append(reversed_pair)
                            visited[str(reversed_pair)] = i
                    if found:
                        break
                    possible = temp
                if found:
                    break
            if not found:
                possible = [pair[1]]
                for i in range(1, 6):
                    temp = []
                    for x in possible:
                        for l, r in ranges:
                            reversed_pair = x[:l] + x[l:r+1][::-1] + x[r+1:]
                            if visited[str(reversed_pair)] != False:
                                solution.append(str(i + visited[str(reversed_pair)]))
                                found = True
                                break
                            temp.append(reversed_pair)
                        if found:
                            break
                        possible = temp
                    if found:
                        break
        print(' '.join(solution))
