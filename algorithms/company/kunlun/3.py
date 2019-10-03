N = int(input())
arr = list(map(int,input().split(" ")))
dic = {}

for item in arr:
    if item not in dic:
        dic[item]=1
    else:
        print(item)