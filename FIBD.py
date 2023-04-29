from collections import defaultdict

n = 82
m = 18

v = defaultdict(lambda: -1)
v[0] = 1
v[1] = 1
v[2] = 1

# Fn = Fn-1 + Fn-2 - Fn-m-1
def fibd(k):
    if k < 0:
        return 0
    if v[k] != -1:
        return v[k]
    v[k] = fibd(k-1) + fibd(k-2) - fibd(k-m-1)
    return v[k]

print(fibd(n))
