p = str(input())
string = str(input())



dp = [[False for i in range(len(p)+1)] for j in range(len(string)+1)]

dp[0][0]= True
for i in range(1,len(p)+1):
    if p[i-1]=='*':
        dp[0][i]=dp[0][i-1]



for i in range(1,len(string)+1):
    for j in range(1,len(p)+1):
        if p[i-1]=='*':
            dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]

        elif p[i-1]=='#':
            dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
        else:
            dp[i][j] = (string[i-1]==p[j-1] or p[j-1]=='?') and dp[i-1][j-1]

if dp[len(string)][len(p)] is True:
    print(1)

else:
    print(0)
