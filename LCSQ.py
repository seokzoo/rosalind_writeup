from collections import defaultdict
from rosalind import rosalind

if __name__ == "__main__":
    with open("data") as f:
        parsed = rosalind.parse_fasta(f.read())
        seqs = list(parsed.values())
        str1 = seqs[0]
        str2 = seqs[1]
        grid = defaultdict(lambda : [[] for _ in range(len(str2) + 1)])

        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                if str1[i-1] == str2[j-1]:
                    grid[i][j] = grid[i-1][j-1] + [str1[i-1]]
                else:
                    if len(grid[i-1][j]) < len(grid[i][j-1]):
                        grid[i][j] = grid[i][j-1]
                    else:
                        grid[i][j] = grid[i-1][j]
        print("".join(grid[len(str1)][len(str2)]))
