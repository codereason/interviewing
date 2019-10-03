weight = int(input())
arr = list(map(int,input().split(" ")))
dp = [-1 for i in range(weight+1)]
dp[0]=0
for i in range(len(arr)):
    for j in range(1,weight+1):
        if j-arr[i]>=0 and dp[j-arr[i]]!=-1:
            dp[j]=1

import sys
if dp[weight]!=-1:
    print ("YES")
    sys.exit()

else:
    print("NO")
    sys.exit()

