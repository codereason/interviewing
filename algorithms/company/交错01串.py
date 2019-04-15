s = list(input())
dp=(len(s)+1)*[-1]
dp[0]=1
for i in range(1,len(s)):
    dp[i] = dp[i-1]+1 if s[i]!=s[i-1] else 1
print(max(dp))