from rosalind import rosalind

def get_reverse_complement(data):
    seq = ''
    for b in data[::-1]:
        match b:
            case 'A':
                seq += 'T'
            case 'T':
                seq += 'A'
            case 'G':
                seq += 'C'
            case 'C':
                seq += 'G'
    return seq

if __name__ == "__main__":
    parsed = rosalind.parse_fasta(open("data").read())
    seq = list(parsed.values())[0]

    for i in range(len(seq)):
        max_idx = 0
        max_seq = ""
        for r in range(4, 13):
            if i+r > len(seq):
                break
            if seq[i:i+r] == get_reverse_complement(seq[i:i+r]):
                print(i+1, r)
