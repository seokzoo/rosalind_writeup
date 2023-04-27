from math import sqrt

k = 2
n = 28
s = sqrt(1+4*k)

print(int((1/s)*(pow(((1+s)/2), n) - pow(((1-s)/2), n))))
