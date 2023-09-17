from Bio.Seq import Seq
from rosalind import rosalind

if __name__ == "__main__":
    with open("data") as f:
        parsed = rosalind.parse_fasta(f.read())
        parsed = list(parsed.values())

        count = 0
        for seq in parsed:
            x = Seq(seq)
            if x == x.reverse_complement():
                count += 1
        print(count)
