from collections import defaultdict

data = open("data").read().strip()
data = data.split("\n")

counter = 0
for i in range(len(data[0])):
    if data[0][i] != data[1][i]:
        counter += 1
print(counter)
