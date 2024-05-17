import copy

if __name__ == "__main__":
    with open("data") as f:
        data = [x.strip() for x in f.readlines()]

        get_threshold = lambda percent, contig : len(''.join(contig)) * percent / 100
        data.sort(key = lambda a : len(a))
        
        ans = []
        for percent in [50, 75]:
            total_length = 0
            d = copy.deepcopy(data)
            while get_threshold(percent, data) > total_length:
                longest = d.pop()
                total_length += len(longest)
            ans.append(str(len(longest)))

        print(' '.join(ans))
