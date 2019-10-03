arr = list(map(int,input().split(",")))
N,left = len(arr),len(arr)-1
dp = [False]*(N-1)+[True]
for i in range(N-2,-1,-1):
    if arr[i]+i>=left:
        left=i
        dp[i] = True
print(1 if dp[0] else 0)