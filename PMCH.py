import math
from rosalind import rosalind

if __name__ == "__main__":
    data = open("data").read()
    parsed = rosalind.parse_fasta(data)
    seq = list(parsed.values())[0]
    count_a = seq.count('A')
    count_g = seq.count('G')

    print(math.factorial(count_a) * math.factorial(count_g))
