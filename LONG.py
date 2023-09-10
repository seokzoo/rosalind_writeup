from rosalind import rosalind

def seq_merger(seq1, seq2):
    longer, shorter = '', ''
    if len(seq1) > len(seq2):
        longer, shorter = seq1, seq2
    else:
        longer, shorter = seq2, seq1
    
    min_length = len(shorter)
    max_length = len(longer)
    min_overlap_length = int(min_length / 2)
    front = shorter[:min_overlap_length]
    end = shorter[-min_overlap_length:]
    front_index, end_index = longer.find(front), longer.find(end)

    if front_index != -1:
        for i in range(max_length):
            if i + min_overlap_length > min_length:
                break
            print(shorter[min_overlap_length + i], longer[-min_overlap_length-i])
        return 2

    if end_index != -1:
        for i in range(max_length):
            shorter_index = min_overlap_length + i + 1
            longer_index = end_index - i - 1
            if longer_index < 0 or shorter_index > min_length:
                break
            print(shorter[-shorter_index], longer[longer_index])

        if i + min_overlap_length == min_length:
            return longer
        elif longer_index < 0:
            return shorter + longer[min_overlap_length + i:]

    return 1

if __name__ == "__main__":
    with open("data") as f:
        parsed_data = rosalind.parse_fasta(f.read())
        seqs = list(parsed_data.values())
        print(seqs)

        while len(seqs) > 1:
            seqs.append(seq_merger(seqs.pop(), seqs.pop()))
