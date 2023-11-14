from rosalind.rosalind import Newick

def traversal(node):
    stack = [node]
    names = []
    while stack:
        current = stack.pop()
        if current.data != None:
            names.append(current.data)
        if current.leaves != None:
            stack += current.leaves
    return names

if __name__ == "__main__":
    with open("data") as f:
        newick_string = f.read().strip()
        newick = Newick(newick_string)
        charset = sorted([x for x in (newick_string.split(';')[0].replace('(', ' ').replace(')', ' ').replace(',', ' ').strip().split(' ')) if x != ''])
        
        stack = [newick.root]
        nodes = []
        while stack:
            current = stack.pop()
            if current != newick.root and current.data == None:
                nodes.append(current)
            if current.leaves != None:
                stack += current.leaves
        
        for node in nodes:
            chartable = [0 for i in range(len(charset))] 
            for name in traversal(node):
                chartable[charset.index(name)] = 1
            print(''.join(map(str, chartable)))
