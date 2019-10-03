a = input().split(" ")
n,m,k=int(a[0]),int(a[1]),int(a[2]) #n是宽 m是长

if m!=n:
    ll = [i for i in range(1,n+1)]+[i for i in range(n,0,-1)]
if m==n:
    ll = [i for i in range(1, n + 1)] + [i for i in range(n-1, 0, -1)]

# print(ll)

t = k
aaa = []
for i in range(len(ll)):
    if t <=ll[i]:
        aaa.append(t)
        aaa.append(i)
    t = t-ll[i]
t,i=aaa[0],aaa[1]


# print(i,t)
#第i层(从0kaishi)

tmp = []
for j in range(i+1):
    if (m - j) * (n - i + j) > 0:
        tmp.append((m-j)*(n-i+j) )
tmp.sort(reverse=True)
# print(tmp)
print(tmp[t-1])
