from itertools import product
from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        splited = f.read().split('\n')[:-1]
        count_dict = defaultdict(lambda : 0)

        for i in [0, 1]:
            splited[i] = list(map(float, splited[i].split(' ')))

        maximal_element = [0, 0]
        for u, v in product(splited[0], splited[1]):
            diff = round(u - v, 7)
            count_dict[diff] += 1
            if count_dict[diff] > maximal_element[0]:
                maximal_element[0] = count_dict[diff]
                maximal_element[1] = diff

        print(maximal_element[0])
        print(abs(maximal_element[1]))
