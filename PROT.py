from collections import defaultdict
# stop : UAA UAG UGA
table = defaultdict(str)
codontable = """UUU F
UUC F
UUA L
UUG L
UCU S
UCC S
UCA S
UCG S
UAU Y
UAC Y
UGU C
UGC C
UGG W
CUU L
CUC L
CUA L
CUG L
CCU P
CCC P
CCA P
CCG P
CAU H
CAC H
CAA Q
CAG Q
CGU R
CGC R
CGA R
CGG R
AUU I
AUC I
AUA I
AUG M
ACU T
ACC T
ACA T
ACG T
AAU N
AAC N
AAA K
AAG K
AGU S
AGC S
AGA R
AGG R
GUU V
GUC V
GUA V
GUG V
GCU A
GCC A
GCA A
GCG A
GAU D
GAC D
GAA E
GAG E
GGU G
GGC G
GGA G
GGG G"""
for c in codontable.split('\n'):
    table[c.split(' ')[0]] = c.split(' ')[1]

data = open('data').read()
for i in range(0, len(data), 3):
    codon = data[i:i+3]
    if codon == "UGA" or codon == "UAA" or codon == "UAG":
        break
    print(table[codon], end="")
print("")
