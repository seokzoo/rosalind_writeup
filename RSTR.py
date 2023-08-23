N = 98979
p = 0.529016

pAT = (1-p)/2
pGC = p/2

SEQ = "AGAAAGAGAC"

cAT = SEQ.count("A") + SEQ.count("T")
cGC = SEQ.count("G") + SEQ.count("C")

print(1 - (1 - (pAT ** cAT)*(pGC ** cGC))**N)
