splited = list(map(int, open("data").read().splitlines()[1].split(' ')))

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        sorted_arr = []
        i, j = 0, 0
        while i < len(left) or j < len(right):
            if i == len(left):
                sorted_arr.append(right[j])
                j += 1
                continue
            elif j == len(right):
                sorted_arr.append(left[i])
                i += 1
                continue

            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        return sorted_arr

print(" ".join(map(str, merge_sort(splited))))
