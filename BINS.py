data = open("data").read().splitlines()

n = int(data[0])
m = int(data[1])

s = list(map(int, data[2].split(' ')))
t = list(map(int, data[3].split(' ')))

def bs(ss, t):
    begin = 0
    idx = int(len(ss)/2)
    end = len(ss)

    while True:
        if ss[idx] > t:
            end = idx
            idx = int((begin + end)/2)
        elif ss[idx] < t:
            begin = idx 
            idx = int((begin + end)/2)
        else:
            return idx + 1
        if begin == idx or end == idx:
            return -1
    
print(' '.join([str(bs(s, x)) for x in t]))
