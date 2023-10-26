if __name__ == "__main__":
    with open("data") as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
        a = (list(map(int, data[1].split(' '))))

        m, l, r = [], [], []
        m.append(a[0])
        for e in a[1:]:
            if a[0] > e:
                l.append(e)
            elif a[0] == e:
                m.append(e)
            else:
                r.append(e)

        print(' '.join(map(str, l + m + r)))
