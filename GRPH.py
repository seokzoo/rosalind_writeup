from collections import defaultdict

data = open("data").read().splitlines()

prefix = defaultdict(list)

s = ''
label = ''
strings = []
for x in data:
    if x[0] == '>':
        if label != '':
            strings.append([label, s])
            s = ''
        label = x[1:]
        continue
    s += x
strings.append([label, s])

for x in strings:
    prefix[x[1][:3]].append(x[0])

for x in strings:
    if prefix[x[1][-3:]] != []:
        for y in prefix[x[1][-3:]]:
            if x[0] != y:
                print(f"{x[0]} {y}")
