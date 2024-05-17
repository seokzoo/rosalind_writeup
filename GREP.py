ans = []

class Mer(object):
    def __init__(self, seq):
        self.seq = seq
        self.next = []

def _traversal(path, current):
    if path[-1] == path[0]:
        ans.append(''.join([step.seq if i == 0 else step.seq[-1] for i, step in enumerate(path[:-len(current.seq)])]))
        return
    for next_mer in current.next:
        if next_mer not in path[1:]:
            _traversal(path + [next_mer], next_mer)

def traversal(path, current):
    for next_mer in current.next:
        _traversal(path + [next_mer], next_mer)
    
if __name__ == "__main__":
    with open("data") as f:
        data = [x.strip() for x in f.readlines()]
        seq_to_mer = {}
        nmer = len(data[0]) - 1

        mers = []
        for seq in data:
            mer = Mer(seq)
            mers.append(mer)
            if seq_to_mer.get(seq):
                seq_to_mer[seq].append(mer)
            else:
                seq_to_mer[seq] = [mer]

        prefix_to_mers = {x[:nmer] : [] for x in data}

        for mer in mers:
            prefix_to_mers[mer.seq[:nmer]].append(mer)

        for seq, imers in seq_to_mer.items():
            for mer in imers:
                mer.next = prefix_to_mers[seq[1:]]
        
        traversal([mers[0]], mers[0])

        ans = list(set(ans))
        ans.sort(key=lambda x: len(x))
        print('\n'.join(([x for x in ans if len(x) == len(ans[-1])])))
