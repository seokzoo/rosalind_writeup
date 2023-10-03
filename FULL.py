amino_dict = {}
get_amino = lambda x: amino_dict.get(str(round(x, 6)))

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
        amino_dict[splited[1]] = splited[0]
    
    with open("data") as f:
        data = list(map(lambda x: float(x.strip()), f.readlines()))
        parent_weight = data[0]
        n = (len(data) - 3)//2
        l = sorted(data[1:])

        print(n)
        for j in range(4):
            w1 = l[0]
            l = l[j:]
            for i in range(1, len(l)):
                possible_set = []
                for e in [x - w1 for x in l[i:]]:
                    c = get_amino(e)
                    if c != None:
                        print(c, end='')
                        possible_set.append(e)
                if possible_set:
                    w1 += possible_set[0]
            print()
