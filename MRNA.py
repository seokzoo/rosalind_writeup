data = open("data").read().replace("\n", "")

codontable = """F
F
L
L
S
S
S
S
Y
Y
C
C
W
L
L
L
L
P
P
P
P
H
H
Q
Q
R
R
R
R
I
I
I
M
T
T
T
T
N
N
K
K
S
S
R
R
V
V
V
V
A
A
A
A
D
D
E
E
G
G
G
G""".split('\n')

n = 3
for x in data:
    n *= codontable.count(x)
    n %= 1000000

print(n)
