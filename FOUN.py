import math
import numpy as np

if __name__ == "__main__":
    with open("data") as f:
        data = list(map(lambda x:list(map(int, x.strip().split(' '))), f.readlines()))
        n, m = data[0]
        calc = lambda i, p : math.comb(2*n, i)*((p)**i)*((1-p)**(2*n-i))
        nfactors = data[1]
       
        markov_matrix = np.array([calc(i, j/(2*n)) for i in range(2*n+1) for j in range(2*n+1)]).reshape(2*n+1,2*n+1)
        p = []
        for nfactor in nfactors:
            p.append(([0 if i != nfactor else 1 for i in range(2*n+1)]))
        p = np.array(p).T

        for _ in range(m):
            next_p = markov_matrix @ p
            print(' '.join(map(str, list(map(math.log10, next_p[0,:])))))
            p = next_p
