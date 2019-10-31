string_input= str(input())
str1,str2 = string_input.split("<ctrip>")
print(str1,str2)
def edit_dist(str1,str2):
    if len(str1) == 0 or len(str2) ==0:
        return max(len(str1),len(str2))
    dp = [[0] * (len(str2)+1) for j in range(0,len(str1)+1)] 
    dp[0][0]=0
    for i in range(0,len(str1)+1):
        for j in range(0,len(str2)+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            else:
                a = dp[i][j-1]+1
                b = dp[i-1][j]+1
                c = 0
                if str1[i-1] == str2[j-1]:
                    c =dp[i-1][j-1]
                else:
                    c = dp[i-1][j-1]+1
                dp[i][j] = min(a,b,c)
    print(dp)
    return dp[-1][-1]

print(edit_dist(str1,str2))