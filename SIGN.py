from collections import defaultdict
from itertools import permutations

data = input()
counter = defaultdict(int)

n = int(data)
e = [x for x in range(1, n+1)]

perm = list(permutations(e, n))
sign = []

for c in perm:
    for i in range(int(pow(2, n))):
        comb = []
        for j in range(n):
            if((i >> j) & 1 == 0):
                comb.append(-c[j])
            else:
                comb.append(c[j])
        sign.append(comb)

print(len(sign))
for p in sign:
    print(" ".join(list(map(str, p))))
