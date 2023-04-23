from collections import defaultdict

data = input()

for b in data[::-1]:
    match b:
        case 'A':
            print("T", end="")
        case 'T':
            print("A", end="")
        case 'G':
            print("C", end="")
        case 'C':
            print("G", end="")
print()
