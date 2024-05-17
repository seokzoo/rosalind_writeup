if __name__ == "__main__":
    with open("data") as f:
        l = list(map(lambda x: list(map(float, x.strip().split(' '))), [line for line in f.readlines()]))
        print(' '.join(map(str, [e * l[0][0] for e in l[1]])))
