n=int(input())
T=list(map(int,input().split()))
T.sort()
flag=False
diff=[]
for i in range(len(T)-1):
    diff.append(T[i+1]-T[i])
if len(set(diff))==1:
    print("Possible")
else:
    print("Impossible")