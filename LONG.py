from rosalind import rosalind

def seq_merger(seq1, seq2, min_overlap_length):
    longer, shorter = '', ''
    if len(seq1) > len(seq2):
        longer, shorter = seq1, seq2
    else:
        longer, shorter = seq2, seq1
    
    min_length = len(shorter)
    max_length = len(longer)
    front = shorter[:min_overlap_length]
    end = shorter[-min_overlap_length:]
    front_index, end_index = longer.find(front), longer.find(end)

    if front_index != -1:
        for i in range(max_length):
            shorter_index = min_overlap_length + i
            longer_index = front_index + min_overlap_length + i
            if shorter[shorter_index] != longer[longer_index]:
                break
            if shorter_index == min_length-1:
                return [longer]
            elif longer_index == max_length-1:
                return [longer[:front_index] + shorter]

    if end_index != -1:
        for i in range(max_length):
            shorter_index = min_overlap_length + i + 1
            longer_index = end_index - i - 1
            if shorter[-shorter_index] != longer[longer_index]:
                break
            if shorter_index == min_length-1:
                return [longer]
            elif longer_index == 0:
                return [shorter + longer[min_overlap_length + i + 1:]]

    return [seq1, seq2]

if __name__ == "__main__":
    with open("data") as f:
        parsed_data = rosalind.parse_fasta(f.read())
        seqs = list(parsed_data.values())

        min_overlap_length = int(len(seqs[0]) / 2)
        
        while len(seqs) > 1:
            for i, seq in enumerate(seqs[1:]):
                r = seq_merger(seqs[0], seq, min_overlap_length)
                if len(r) == 1:
                    seqs = seqs[1:]
                    del seqs[i]
                    seqs.append(r[0])
                    break
        print(seqs[0])
