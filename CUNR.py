import math

def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
        if prod % 1000000 != 0:
            prod %= 1000000
    return prod

if __name__ == "__main__":
    with open("data") as f:
        n = int(f.read())

        if n == 1 or n == 2:
            print(1)
        else:
            a = fact(2*n-4)
            b = fact(n-2)
            c = (2**(n-2))
            print((a // c) // b % 1000000)
