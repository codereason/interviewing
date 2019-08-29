sss= input()
h = list(map(int,input().split()))
n,m = sss.split(" ")[0],sss.split(" ")[1]
ll = []
# print(n,m,h)

for i in range(len(h)-1):
    # print(i)
    ll.append(h[i+1] - h[i])

ll.sort()
print(ll)
print(ll[int(m)-1])