class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.leaves = []

class Newick(object):
    def __init__(self, newick_string):
        self.root = Node(None)
        string = newick_string.replace(' ', '').replace(',,', ',  ,').replace('(,', '(  ,').replace(',)', ',  )')
        indices = [i for i, c in enumerate(string) if c in ['(', ')', ',', ';']]
        tokenized = []
        start = 0
        for i, idx in enumerate(indices):
            name = string[start:idx]
            if name:
                tokenized.append(name)
            if string[idx] == ';':
                break
            tokenized.append(string[idx])
            start = idx + 1
        current = self.root
        for i, token in enumerate(tokenized):
                if token ==  '(':
                    node = Node(None)
                    node.parent = current
                    current.leaves.append(node)
                    current = node
                elif token == ',':
                    current = current.parent
                    node = Node(None)
                    node.parent = current
                    current.leaves.append(node)
                    current = node
                elif token ==  ')':
                    current = current.parent
                else:
                    current.data = token

    def find(self, value_string):
        return self._find(self.root, value_string)

    def _find(self, node, value_string):
        stack = []
        stack.append(self.root)
        while stack:
            current = stack.pop()
            if current.data == value_string:
                return current
            stack += current.leaves
        return

    def distance(self, a_string, b_string):
        a = self.find(a_string)
        b = self.find(b_string)
        current = a
        path = []
        while current != None:
            path.append(id(current))
            current = current.parent
        current = b
        count = 0
        while current != None:
            if id(current) in path:
                return path.index(id(current)) + count
            current = current.parent
            count += 1
        return

if __name__ == "__main__":
    with open("data") as f:
        data = f.read()
        data = list(map(lambda x: x.split('\n'), data.strip().split("\n\n")))
        newicks = []
        test = []
        for x in data:
            newicks.append(x[0])
            test.append(x[1])

        solution = []
        for i, newick_string in enumerate(newicks):
            newick = Newick(newick_string)
            a, b = test[i].split(' ')
            solution.append(str(newick.distance(a, b)))
        print(' '.join(solution))
