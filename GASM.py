from rosalind.rosalind import get_rc
from collections import deque

if __name__ == "__main__":
    with open("data") as f:
        lines = f.read().strip().split('\n')
        
        cycle = deque()
        S = []
        for line in lines:
            rc = get_rc(line)
            S.append((line, rc))

        cycle.append(S.pop()[0])
        n = len(cycle[0])
        string = cycle[0]

        while S:
            found = False
            for i in range(n):
                s = i + 1
                for mer in S:
                    for x in mer:
                        if x[:n-s] == cycle[-1][s:]:
                            string += x[n-s:]
                            cycle.append(x)
                            S.remove(mer)
                            found = True
                            break
                        if x[s:] == cycle[0][:n-s]:
                            string = x[:s] + string
                            cycle.appendleft(x)
                            S.remove(mer)
                            found = True
                            break
                    if found == True:
                        break
                if found == True:
                    break
    for i in range(n):
        l = n - i
        if string[l:].find(string[:l]) != -1:
            print(string[l:])
            break
