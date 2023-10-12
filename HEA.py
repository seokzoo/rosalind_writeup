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
        print(' '.join([str(heap[i]) for i in range(1, n+1)]))
