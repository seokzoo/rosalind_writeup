
if __name__ == "__main__":
    with open("data") as f:
        data = f.readlines()
        data = list(map(lambda x: x.strip(), data)) 
        n = int(data[0])
        s = data[1]
        GC_ratio_list = list(map(float, data[2].split(' ')))

        GC_count = s.count('G') + s.count('C')
        AT_count = s.count('T') + s.count('A')

        ans = []
        for r in GC_ratio_list:
            a = (r/2)**GC_count 
            b = ((1-r)/2)**AT_count
            ans.append(str(round(a*b*(n-1), 5)))
        print(' '.join(ans))
