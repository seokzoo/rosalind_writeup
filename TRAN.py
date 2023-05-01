data = open("data").read().splitlines()

s = ''
strings = []
for x in data:
    if x[0] == '>':
        if s != '':
            strings.append(s)
            s = ''
        continue
    s += x
strings.append(s)

def det(a, b):
    if a == b:
        return 0
    match(a, b):
        case ('A', 'G'):
            return -1
        case ('T', 'C'):
            return -1
        case ('G', 'A'):
            return -1
        case ('C', 'T'):
            return -1
    return 1

tn = 0
tv = 0
for i in range(len(strings[0])):
    d = det(strings[0][i], strings[1][i])
    if d == -1:
        tn += 1
    elif d == 1:
        tv += 1
print(tn/tv)
