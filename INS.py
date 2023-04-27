
data = open("data").read().split('\n')
vv = list(map(int, data[1].split(' ')))
count = 0

for k in range(1, len(vv)):
    while k > 0 and vv[k] < vv[k-1]:
        count += 1
        vv[k-1] ^= vv[k]
        vv[k] ^= vv[k-1]
        vv[k-1] ^= vv[k]
        k -= 1
print(count)
