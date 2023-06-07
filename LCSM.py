import itertools
from collections import defaultdict
from rosalind import rosalind

def get_shared_motifs(str1, str2):
    grid = defaultdict(lambda : [0 for _ in range(len(str2))])

    shared_motifs = []
    for i in range(len(str1)):
        c1 = str1[i]
        for j in range(len(str2)):
            c2 = str2[j]
            if c1 != c2:
                grid[i][j] = 0
            else:
                if i == 0 and j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i-1][j-1] + 1
            length = grid[i][j]
            if length >= 2:
                shared_motifs.append(str1[i - length + 1 : i + 1])

    return shared_motifs

if __name__ == "__main__":
    with open("data") as f:
        parsed = rosalind.parse_fasta(f.read())
        seqs = [s for s in parsed.values()]

        str1 = seqs.pop()
        str2 = seqs.pop()

        shared_motifs = set(get_shared_motifs(str1, str2))
        for seq in seqs:
            for motif in list(shared_motifs):
                if seq.find(motif) == -1:
                    shared_motifs.remove(motif)
        m = list(shared_motifs)
        m.sort(key=len)
        LCSM = m[-1]

        print(LCSM)
