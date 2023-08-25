class Node(object):
    adj_list = []
    def __init__(self, label):
        self.label = label
        self.children = {}
    def add_child(self, node, value):
        self.children[value] = node
        Node.adj_list.append([self.label, node.label, value])

with open("data") as f:
    data = f.read().splitlines()

    root = Node(1)
    count = 2
    for seq in data:
        current = root
        for x in seq:
            if x in current.children:
                current = current.children[x]
            else:
                node = Node(count)
                current.add_child(node, x)
                current = node
                count += 1
    for x in root.adj_list:
        print(' '.join(map(str, x)))
