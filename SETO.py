
if __name__ == "__main__":
    splited = open("data").read().splitlines()
    n = int(splited[0])
    A = set(map(int, splited[1].translate(str.maketrans('{}', ',,')).replace(',', '').split()))
    B = set(map(int, splited[2].translate(str.maketrans('{}', ',,')).replace(',', '').split()))
    U = set([i for i in range(1, n+1)])

    print(A.union(B))
    print(A.intersection(B))
    print(A - B)
    print(B - A)
    print(U - A)
    print(U - B)
