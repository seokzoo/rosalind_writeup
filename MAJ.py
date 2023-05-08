from collections import defaultdict

data = open("data").read().splitlines()

ans = []
for l in data[1:]:
    arr = list(map(int, l.split(' ')))
    count = defaultdict(lambda: 0)
    ans.append(-1)
    for x in arr:
        count[x] += 1
        if count[x] > (len(arr) // 2):
            ans.pop()
            ans.append(x)
            break

print(' '.join(list(map(str, ans))))
