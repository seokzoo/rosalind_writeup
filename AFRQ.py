import math

if __name__ == "__main__":
    with open("data") as f:
        ratio_list = list(map(float, f.read().split(' ')))
        size = len(ratio_list)
        # (p + q)^2 = p^2 + 2pq + q^2
        # q^2 = x, p = (1 - sqrt(x))
        ans_list = []
        for x in ratio_list:
            p = math.sqrt(x)
            ans = (1 - (1-p) * (1-p))
            ans_list.append(ans)
        print(' '.join(map(str, ans_list)))
