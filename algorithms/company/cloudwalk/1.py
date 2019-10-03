

aa = list(map(int,input().split(",")))

fp = [1]*len(aa)
for i in range(1,len(aa)):
    for j in range(0,i):
        if aa[j] < aa[i]:
            fp[i] = max(fp[i],fp[j]+1)


print(max(fp))