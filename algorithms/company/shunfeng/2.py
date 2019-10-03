import math

b = str(input())
a=[]
b = b.split(':')
a = []
w = []
m = 0
s = ''
fen = ''
if b[0].isdecimal():
    for x in b[0]:
        a.append(int(x))
        s += x
else:
    for x in b[0]:
        if x.isalpha():
            s += str(int(ord(x)) - 55)
            a.append(int(ord(x)) - 55)
        else:
            s += x
            a.append(int(x))

if b[1].isdecimal():
    for x in b[1]:
        a.append(int(x))
        fen += x
else:
    for x in b[1]:
        if x.isalpha():
            fen += str(int(ord(x)) - 55)
            a.append(int(ord(x)) - 55)
        else:
            fen += x
bs = int(s)
bf = int(fen)
m = int(max(a)) + 1
while True:
    f = int(str(bf), m)
    if f > 59:
        break
    else:
        f = int(str(bs), m)
        if f < 24:
            w.append(str(m))
        else:
            break
    m += 1

print(" ".join(str(item) for item in w))