from rosalind import rosalind
from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        parsed = rosalind.parse_fasta(f.read())
        seq = [x for x in parsed.values()][0]
        grid = defaultdict(lambda : 0)

        nmer = 4
        trans = str.maketrans("ACGT", "0123")

        # ACGT
        for i in range(len(seq)-(nmer-1)):
            mer = seq[i:i+nmer]
            k = 0
            for j, b in enumerate(mer[::-1]):
                k += int(b.translate(trans)) * (4**j)
            grid[k] += 1

        print(' '.join(list(map(str, [grid[i] for i in range(4**4)]))))
            
