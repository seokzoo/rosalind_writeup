from rosalind import rosalind
from collections import defaultdict

def failure_function(seq):
    failure_array = defaultdict(lambda : 0)
    i, j = 0, 1
    while j < len(seq):
        if seq[i] == seq[j]:
            failure_array[j] = failure_array[j] + i + 1
            j += 1
            i += 1
        elif i > 0:
            i = failure_array[i-1]
        else:
            i = 0
            j += 1
    return [failure_array[i] for i in range(len(seq))]

if __name__ == "__main__":
    with open("data") as f:
        parsed_data = rosalind.parse_fasta(f.read())
        seq = list(parsed_data.values())[0]
        failure_array = failure_function(seq)
        print(' '.join(map(str, failure_array)))
