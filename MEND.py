from rosalind.rosalind import *
from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        newick = Newick(f.read())
        root = newick.root                  
        stack = [(0, root)]
        bydepth = defaultdict(list)

        while stack:
            n, current = stack.pop()
            if current.data != None:
                factor = current.data
                if factor == "AA":
                    current.data = (1, 0, 0)
                elif factor == "Aa":
                    current.data = (0, 1, 0)
                elif factor == "aa":
                    current.data = (0, 0, 1)
                bydepth[n].append(current)
            stack += [(n+1, x) for x in current.leaves]
        while not bydepth[0]:
            depth = max(bydepth.keys())
            nodes = bydepth[depth]
            while nodes:
                node = nodes.pop()
                parent = node.parent
                pair_node = list(set(parent.leaves) - set([node]))[0]
                nodes.remove(pair_node)
                a, b, c = node.data
                A, B, C = pair_node.data
                AA = a*A + b*B/4 + a*B/2 + A*b/2
                Aa = a*B/2 + A*b/2 + A*c + a*C + b*C/2 + B*c/2 + b*B/2
                aa =  c*C + b*C/2 + B*c/2 + b*B/4
                parent.data = (AA, Aa, aa)
                bydepth[depth-1].append(parent)
            del bydepth[depth]
        print(' '.join(map(str, bydepth[0][0].data)))
