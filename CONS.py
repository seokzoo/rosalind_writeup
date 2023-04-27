from collections import defaultdict

data = open("data").read().strip().split('\n')
profile = defaultdict(lambda: defaultdict(int))

m = []
chunk = ''
for x in data:
    if x[0] == '>':
        if chunk != '':
            m.append(chunk)
        chunk = ''
        continue
    chunk += x
m.append(chunk)

for s in m:
    for j, b in enumerate(s):
        profile[b][j] += 1

for i in range(len(m[0])):
    c = ''
    highest = 0
    for b in ['A', 'C', 'G', 'T']:
        if highest < profile[b][i]:
            highest = profile[b][i]
            c = b
    print(f"{c}", end="")
print("")

for b in ['A', 'C', 'G', 'T']:
    p = [profile[b][i] for i in range(len(m[0]))]
    print(f'{b}: ' + ' '.join(list(map(str, p))))
