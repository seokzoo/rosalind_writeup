data = open("data").read().splitlines()

a = list(map(int, data[1].split(' ')))
b = list(map(int, data[3].split(' ')))
m = []

i, j = 0, 0
for _ in range(len(a) + len(b)):
    if len(a) <= i:
        m += b[j:]
        break
    if len(b) <= j:
        m += a[i:]
        break

    if a[i] < b[j]:
        m.append(a[i])
        i += 1
    else:
        m.append(b[j])
        j += 1

print(' '.join((map(str, m))))
