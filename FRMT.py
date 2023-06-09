from Bio import Entrez
from rosalind import rosalind

if __name__ == "__main__":
    ids = open("data").read().split()
    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
    parsed = rosalind.parse_fasta(handle.read())
    
    longest = ''
    longest_length = float("inf")
    for label, seq in parsed.items():
        if longest_length > len(seq):
            longest = label
            longest_length = len(seq)
    print('>' + longest)
    print(parsed[longest])

