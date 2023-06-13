import math
from rosalind import rosalind

if __name__ == "__main__":
    parsed = rosalind.parse_fasta(open("data").read())
    seq = list(parsed.values())[0]
    count = [seq.count(b) for b in ['A', 'U', 'G', 'C']]
    m = max(count[0], count[1])
    n = min(count[0], count[1])

    a = 1
    for i in range(1, n+1):
        a *= math.comb(m-i+1, 1)

    m = max(count[2], count[3])
    n = min(count[2], count[3])

    b = 1
    for i in range(1, n+1):
        b *= math.comb(m-i+1, 1)

    print(a * b)
