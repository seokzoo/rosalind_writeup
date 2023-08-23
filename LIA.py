import math

k = 7
n = 34

p = 0
for i in range(n, 2**k + 1):
    population = pow(2, k)
    p += math.comb(population, i) * ((1/4)**i) * ((3/4)**(population-i))

print(p)
