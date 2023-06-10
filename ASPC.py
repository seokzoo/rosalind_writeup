import math

n = 1867
k = 674

s = 0
for i in range(k, n+1):
    s = (s + math.comb(n, i)) % 1000000

print(s)
