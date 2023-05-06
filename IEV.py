from math import comb

data = list(map(int, open("data").read().split(' ')))
gtype = [1, 1, 1, 3/4, 1/2, 0]

e = [data[i] * gtype[i] * 2 for i in range(6)]

print(sum(e))
