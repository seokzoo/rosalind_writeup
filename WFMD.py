import math
from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        n, m, g, k = list(map(int, f.read().split(' ')))
        p = m/(2*n)
        p = 1 - p
        calc = lambda i, p : math.comb(2*n, i)*((p)**i)*((1-p)**(2*n-i))

        # at least 1 copies of a recessive allele
        vec = defaultdict(lambda : 0)
        vec2 = defaultdict(lambda : 0)

        for i in range(1, 2*n+1):
            vec[i] = calc(i, p) 
        
        for _ in range(g-1):
            for j in range(1, 2*n+1):
                for i in range(1, 2*n+1):
                    vec2[j] += vec[i] * calc(j, i/(2*n))
            vec = vec2
            vec2 = defaultdict(lambda : 0)
        print(sum([vec[i] for i in range(k, 2*n+1)]))
