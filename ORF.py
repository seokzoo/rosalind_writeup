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

RNA = ''.join(open('data').read().split('\n')[1:]).replace("T", "U")

def find_all(string, pattern):
    i = 0
    j = 0
    idxs = []
    while(True):
        i = string[j:].find(pattern)
        if(i == -1):
            break
        j = j + i + 1
        idxs.append(j - 1)
    return idxs

ORFS = []

start = find_all(RNA, 'AUG')
for idx in start:
    ORF = ''
    for i in range(idx, len(RNA), 3):
        codon = RNA[i:i+3]
        if codon == "UGA" or codon == "UAA" or codon == "UAG":
            ORFS.append(ORF)
            break
        amino = table[codon]
        ORF += amino

REVC = ''
for b in RNA[::-1]:
    match b:
        case 'A':
            REVC += "U"
        case 'U':
            REVC += "A"
        case 'G':
            REVC += "C"
        case 'C':
            REVC += "G"

RNA = REVC
start = find_all(RNA, 'AUG')
for idx in start:
    ORF = ''
    for i in range(idx, len(RNA), 3):
        codon = RNA[i:i+3]
        if codon == "UGA" or codon == "UAA" or codon == "UAG":
            ORFS.append(ORF)
            break
        amino = table[codon]
        ORF += amino

for x in list(set(ORFS)):
    print(x)
