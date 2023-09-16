from rosalind import rosalind

def get_reverse_complement(seq):
    rc = ""
    for n in seq:
        if n == 'A':
            rc += 'T'
        elif n == 'T':
            rc += 'A'
        elif n == 'G':
            rc += 'C'
        elif n == 'C':
            rc += 'G'
    return rc[::-1]

def get_hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        raise Exception("[!] strings are different in length")
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

if __name__ == "__main__":
    with open("data") as f:
        parsed = rosalind.parse_fasta(f.read())
        seqs = list(parsed.values())
        candidate_list = []
        correctly_sequenced_list = []

        for seq in seqs:
            rc = get_reverse_complement(seq)
            if rc not in candidate_list:
                candidate_list.append(seq)
            if rc in seqs or seqs.count(seq) >= 2:
                correctly_sequenced_list.append(seq)
                correctly_sequenced_list.append(rc)
        correctly_sequenced_list = list(set(correctly_sequenced_list))
        candidate_list = list(set(candidate_list) - set(correctly_sequenced_list))

        for x in candidate_list:
            for y in correctly_sequenced_list:
                if get_hamming_distance(x, y) == 1:
                    print(f"{x}->{y}")
