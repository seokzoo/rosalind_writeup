from collections import defaultdict
from itertools import permutations

data = input()
counter = defaultdict(int)

n = int(data)
perm = list(permutations([x for x in range(1, n+1)], n))
print(len(perm))
for p in perm:
    print(" ".join(list(map(str, p))))
