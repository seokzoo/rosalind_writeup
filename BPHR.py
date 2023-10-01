from Bio.SeqIO import parse
from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        threshold = int(f.readline())

        q = defaultdict(lambda : 0)
        parsed = parse(f, "fastq")
        count = 0
        for x in parsed:
            count += 1
            r = x.letter_annotations["phred_quality"]
            for i, y in enumerate(r):
                q[i] += y
        print(sum([(q[i] / count) < threshold for i in range(len(q))]))
