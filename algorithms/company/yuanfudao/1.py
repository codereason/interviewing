# num = int(input())

xxx = input()
length1 = int(xxx.split(" ")[0])
m = int(xxx.split(" ")[1])

h = list(map(int,input().split()))


dict1 = {}

for i in h:
    if i not in dict1:
        dict1[i] =1
    else:
        dict1[i]+=1

aaa = []
for num in h:
    if dict1[num]<=m:
        aaa.append(num)
print(" ".join([str(item) for item in aaa]))
