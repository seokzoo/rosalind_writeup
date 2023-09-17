
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

    with open("data") as f:
        data = f.readlines()
        data = list(map(lambda x : float(x.strip()), data))

        k = sorted(data)
        for i in range(len(k)-1):
            d = k[i+1] - k[i]
            for i, w in enumerate(mc_ratio_list):
                if abs(d - w) < 0.001:
                    print(amino_list[i], end="")
                    break
        print('')
