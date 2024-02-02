import itertools

amino_dict = {}
get_amino = lambda x: amino_dict.get(str(round(x, 4)))

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

if __name__ == "__main__":
    table = '''A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333'''
    table = table.split('\n')
    mc_ratio_list = []
    amino_list = []
    for i, x in enumerate(table):
        splited = x.split('   ')
        amino_list.append(splited[0])
        mc_ratio_list.append(float(splited[1]))
        amino_dict[str(round(float(splited[1]), 4))] = splited[0]
    
    with open("data") as f:
        l = list(map(float, f.readlines()))
        nodes = []
        for weight in l:
            nodes.append(Node(weight))    

        visited = set()
        internals = set()

        for u, v in itertools.combinations(nodes, 2):
            diff = abs(u.value - v.value)
            amino = get_amino(diff)
            if amino != None:
                visited.add(u)
                visited.add(v)
                if u.value > v.value:
                    v.edges.append((amino, u))
                    internals.add(u)
                else:
                    u.edges.append((amino, v))
                    internals.add(v)
        roots = list((set(nodes) & visited) - internals)
        longest_path = ''
        queue = []
        for root in roots:
            queue.append(('', root))

        while queue:
            seq, node = queue.pop()    
            if not node.edges:
                if len(longest_path) < len(seq):
                    longest_path = seq
            for amino, dest in node.edges:
                queue.append((seq + amino, dest))
        print(longest_path)
