data = open("data").read().splitlines()

s = ''
strings = []
for x in data:
    if x[0] == '>':
        if s != '':
            strings.append(s)
        s = ''
    else:
        s += x
strings.append(s)


idx = 0
indices = []
for b in strings[1]:
    idx = strings[0][idx:].find(b) + idx + 1
    indices.append(idx)

print(' '.join(map(str, indices)))
