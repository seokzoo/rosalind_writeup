from rosalind import rosalind
from collections import defaultdict

if __name__ == "__main__":
    parsed = rosalind.parse_fasta(open("data").read())
    seqs = (list(parsed.values()))
    matrix = defaultdict(lambda : [0.0 for _ in range(len(seqs))])

    for i in range(len(seqs)):
        for j in range(i, len(seqs)):
            if i == j:
                matrix[i][j] = 0.0
            else:
                error_count = sum([seqs[i][k] != seqs[j][k] for k in range(len(seqs[0]))])
                p_distance = error_count / len(seqs[0])
                matrix[i][j] = p_distance
                matrix[j][i] = p_distance

    for i in range(len(seqs)):
        for j in range(len(seqs)):
            print(matrix[i][j], end="")
            if j != len(seqs) - 1:
                print(" ", end="")
        print()
