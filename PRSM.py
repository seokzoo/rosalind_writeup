from itertools import product
from collections import defaultdict

if __name__ == "__main__":
    table_text = '''A   71.03711
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
    table = {}
    table_text = table_text.split('\n')
    for i, x in enumerate(table_text):
        splited = x.split('   ')
        table[splited[0]] = float(splited[1])
        
    with open("data") as f:
        n = int(f.readline())
        data = f.readlines()
        data = list(map(lambda x : x.strip(), data))
        strings = data[:n]
        weighted_strings = []
        r = list(map(float, data[n:]))
        for string in strings: 
            weighted_string = []
            for c in string:
                weighted_string.append(table[c])
            weighted_strings.append(weighted_string)

        specs = []
        for x in weighted_strings:
            spec = []
            spec.append(sum(x))
            for i in range(1, len(x)-1):
                spec.append(sum(x[:i]))
                spec.append(sum(x[-i:]))
            specs.append(spec)

        maximum = [0, 0]
        for i, x in enumerate(specs):
            count_dict = defaultdict(lambda : 0)
            maximal_element = [0, 0]
            for u, v in product(r, x):
                diff = round(u - v, 7)
                count_dict[diff] += 1
                if count_dict[diff] > maximal_element[0]:
                    maximal_element[0] = count_dict[diff]
                    maximal_element[1] = diff
            if maximal_element[0] >= maximum[0]:
                maximum[0] = maximal_element[0]
                maximum[1] = i

        print(maximum[0])
        print(strings[maximum[1]])
