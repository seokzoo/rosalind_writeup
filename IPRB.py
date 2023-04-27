from math import comb

a = 15
b = 21
c = 26

l = comb(c, 2)*4 + comb(2*c, 1)*comb(b, 1) + comb(b, 2)
m = 4*a*b + 4*a*c + 4*b*c + comb(a, 2)*4 + comb(b, 2)*4 + comb(c, 2)*4

print(1 - l/m)
