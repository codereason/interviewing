import sys
kkk = []
try:
    line = sys.stdin.readline().strip()
    N,M  = int(line.split(" ")[0]) , int(line.split(" ")[1])

    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

        a = int(line)
        kkk.append(a)

except:
    pass
##kkk是D

def helper(d,index,pos,n,flag):
    if index>=len(d) and pos>=0 and pos<=n:
        s.add(pos)
        return
    if d[index]<=pos:
        helper(d, index + 1, pos - d[index], n, flag)

    if (d[index] <= n - pos - 1):
        helper(d, index + 1, pos + d[index], n, flag)

s = set()
for i in range(N):
    helper(kkk, 0, i, N, i)
print(len(s))