from itertools import product
from collections import defaultdict

data = open("data").read().split("\n")

# 0 means nothing
symbols = ['0']
symbols += data[0].split(' ')
n = int(data[1])
k = len(symbols)

s = [symbols] * n

strings = []
for pd in product(*s):
    flag = 0
    for i, x in enumerate(pd):
        if pd[0] == '0' or (i != 0 and pd[i] != '0' and pd[i-1] == '0'):
            flag = 1

            break
    if flag == 0:
        strings.append(''.join(list(pd)).replace('0', ''))

for x in strings:
    print(x)
