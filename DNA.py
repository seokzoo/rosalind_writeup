from collections import defaultdict

data = input()
counter = defaultdict(int)

for b in data:
    counter[b] += 1

print(counter['A'], end=" ")
print(counter['C'], end=" ")
print(counter['G'], end=" ")
print(counter['T'])
