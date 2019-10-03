line1 = input()
N,M,K = int(line1.split()[0]),int(line1.split()[1]),int(line1.split()[2])

res = set()
def dfs(tmp,n,m):
    if tmp.count('a')<= n and tmp.count('b')<=m  :
        res.add(tmp[:])
    else:
        return

    tmp+='a'
    dfs(tmp,n,m)
    tmp=tmp[:len(tmp)-1]
    tmp+='b'
    dfs(tmp,n,m)
    tmp=tmp[:len(tmp)-1]
tmp = ""
dfs(tmp,N,M)
print(sorted(list(res))[K])

max_length = M+N
ll = K//max_length,K%max_length
