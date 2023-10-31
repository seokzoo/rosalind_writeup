from collections import defaultdict

if __name__ == "__main__":
    with open("data") as f:
        data = list(map(lambda x: x.strip(), f.readlines()))
        n = int(data[0])
        arr = list(map(int, data[1].split(' ')))
        heap = defaultdict(lambda : 0)

        for i in range(1, n+1):
            heap[i] = arr[i-1]
            if i != 0:
                current = i
                while current > 1:
                    if heap[current//2] < heap[current]:
                        tmp = heap[current//2] 
                        heap[current//2] = heap[current]
                        heap[current] = tmp
                    current = current // 2
        h = [None] + [heap[i] for i in range(1, n+1)]
        solution = []
        for i in range(n):
            solution.append(h[1])
            h[1] = h.pop()
            current = 1
            if len(h) == 2:
                solution.append(h[1])
                break
            elif len(h) == 3:
                solution.append(max(h[1], h[2]))
                solution.append(min(h[1], h[2]))
                break
            while h[current*2] > h[current] or h[min(current*2+1, len(h)-1)] > h[current]:
                if h[current*2] >= h[min(current*2+1, len(h)-1)]:
                    current = current*2
                else:
                    current = current*2+1
                tmp = h[current//2] 
                h[current//2] = h[current]
                h[current] = tmp
                if current*2 >= len(h):
                    break
        print(' '.join(map(str, solution[::-1])))
