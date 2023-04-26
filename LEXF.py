from collections import defaultdict
from itertools import permutations, product

data = open("data").read().strip()
data = data.split('\n')

perm = list(product(data[0].split(" "), repeat = int(data[1])))

for p in perm:
    print("".join(list(map(str, p))))
