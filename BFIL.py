from Bio.SeqIO import parse
from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        threshold = int(f.readline())

        q = defaultdict(lambda : 0)
        parsed = parse(f, "fastq")
        for x in parsed:
            name = x.id
            seq = x.seq
            r = x.letter_annotations["phred_quality"]

            left_idx = 0
            right_idx = 0
            for i, s in enumerate(r):
                if s >= threshold:
                    left_idx = i
                    break
            for i, s in enumerate(r[::-1]):
                if s >= threshold:
                    right_idx = i
                    break
            if left_idx == len(r) - 1:
                a = seq
                b = r
            else:
                a = seq[left_idx:-right_idx]
                b = r[left_idx:-right_idx]
            print('@' + name)
            print(a)
            print('+')
            print(''.join([chr(e+33) for e in b]))
