from math import factorial as ft

n = 87
k = 9

print(int(ft(n)/ft(n-k)) % 1000000)
