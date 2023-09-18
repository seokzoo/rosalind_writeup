import math

if __name__ == "__main__":
    n = 41
    total = n*2
    p_list = []
    for i in range(1, total + 1):
        p = 0
        for j in range(i, total + 1):
            p += math.comb(total, j)*((1/2)**total)
        p_list.append(math.log(p, 10))

    print(' '.join(map(str, p_list)))
