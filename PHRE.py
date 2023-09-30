from Bio.SeqIO import parse

if __name__ == "__main__":
    with open("data") as f:
        threshold = int(f.readline())

        average = []
        for x in parse(f, "fastq"):
            r = x.letter_annotations["phred_quality"]
            average.append(sum(r) / len(r))
        print(sum([1 for x in average if x < threshold]))
