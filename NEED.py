from Bio import Entrez, SeqIO
from Bio import Align
from Bio.Emboss.Applications import NeedleCommandline

if __name__ == "__main__":
    with open("data") as f:
        seqs = []
        for x in f.read().split(' '):
            handle = Entrez.efetch(db="nucleotide", id=x, rettype="fasta", retmode="text")
            record = SeqIO.read(handle, "fasta")
            seqs.append(record.seq)

        print(str(seqs[0]))
        print()
        print(str(seqs[0]))
