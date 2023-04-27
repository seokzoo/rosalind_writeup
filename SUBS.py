def find_all(string, pattern):
    i = 0
    j = 0
    idxs = []
    while(True):
        i = string[j:].find(pattern)
        if(i == -1):
            break
        j = j + i + 1
        idxs.append(j)
    return idxs

data = open("data").read().split('\n')

print(' '.join(list(map(str, find_all(data[0], data[1])))))
