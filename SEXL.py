
if __name__ == "__main__":
    with open("data") as f:
        prop_list = list(map(float, f.read().split(' ')))

        ans = []
        for p in prop_list:
            x = p*(1-p)*2
            ans.append(x)
        print(' '.join(map(str, ans)))
