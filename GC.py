data = open("data").read().replace("\n", "").split(">Rosalind_")[1:]

highest = ["", 0]
for s in data:
    ratio = (s[4:].count('G') + s[4:].count('C'))/len(s[4:])*100
    if ratio > highest[1]:
        highest[0] = s[:4]
        highest[1] = ratio

print(f"Rosalind_{highest[0]}\n{highest[1]}")
