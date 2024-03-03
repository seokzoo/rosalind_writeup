from collections import defaultdict, deque
from itertools import combinations
import math

stoi = lambda x: [i-1 for i in list(map(int, x.split(' ')))]
ltoi = lambda x: sum([i*((10)**n) for n, i in enumerate(x)])

if __name__ == "__main__":
    with open("data") as f:
        path = []
        x = f.read().strip().split('\n')
        length = 10
        pair = [stoi(x[0]), stoi(x[1])]
        possible = deque()
        visited = set()
        ranges = list(combinations([i for i in range(length)], 2))
        found = False
        if pair[0] == pair[1]:
            print('0')
        else:
            for l, r in ranges:
                reversed_pair = pair[0][:l] + pair[0][l:r+1][::-1] + pair[0][r+1:]
                if reversed_pair == pair[1]:
                    path = [(l, r)]
                    found = True
                    break
                possible.appendleft(([(l, r)], reversed_pair))
            if not found:
                while possible:
                    rev, x = possible.pop()
                    if len(visited) > math.factorial(10) // 2:
                        break
                    for l, r in ranges:
                        reversed_pair = x[:l] + x[l:r+1][::-1] + x[r+1:]
                        if reversed_pair == pair[1]:
                            path = rev + [(l, r)]
                            found = True
                            break
                        if ltoi(reversed_pair) not in visited:
                            visited.add(ltoi(reversed_pair))
                            possible.appendleft((rev + [(l, r)], reversed_pair))
                    if found:
                        break

            if not found:
                possible2 = deque()
                for l, r in ranges:
                    reversed_pair = pair[1][:l] + pair[1][l:r+1][::-1] + pair[1][r+1:]
                    possible2.appendleft(([(l, r)], reversed_pair))
                visited2 = set()
                while possible2:
                    rev, x = possible2.pop()
                    for l, r in ranges:
                        reversed_pair = x[:l] + x[l:r+1][::-1] + x[r+1:]
                        if ltoi(reversed_pair) in visited:
                            for p, pair in possible:
                                if pair == reversed_pair:
                                    path = p + list(reversed(rev + [(l, r)]))
                                    break
                            found = True
                            break
                        if ltoi(reversed_pair) not in visited2:
                            visited2.add(ltoi(reversed_pair))
                            possible2.appendleft((rev + [(l, r)], reversed_pair))
                    if found:
                        break

            print(len(path))
            for step in path:
                print(f'{step[0]+1} {step[1]+1}') 
