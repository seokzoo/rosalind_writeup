from math import log10

data = open("data").read().splitlines()

s = data[0]
A = list(map(float, data[1].split(' ')))

ans = []
for x in A:
    p = 1
    for b in s:
        if b == 'A' or b == 'T':
            p *= (1-x)/2
        elif b == 'G' or b == 'C':
            p *= x/2
    ans.append(log10(p))

print(' '.join(list(map(str, ans))))
