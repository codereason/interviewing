import sys
kkk = []
cov = []
try:
    line = sys.stdin.readline().strip()
    h, w = int(line.split(" ")[0]) , int(line.split(" ")[1])
    kkk.append([h,w])
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

        a = list(map(int, line.split(' ')))
        kkk.append(a)

except:
    pass

kkk = kkk[1:]
res = []

l,u,d,r = 0,0,len(kkk)-1,len(kkk[0])-1
while l<=r and u<=d:
    for i in range(l,r+1):
        res.append(kkk[u][i])
    u+=1
    for i in range(u,d+1):
        res.append(kkk[i][r])
    r-=1
    for i in reversed(range(l,r+1)):
        res.append(kkk[d][i])

    d -=1
    for i in reversed(range(u,d+1)):
        res.append(kkk[i][l])

    l+=1
res = res[:len(kkk)*len(kkk[0])]
print(",".join(str(item) for item in res))

