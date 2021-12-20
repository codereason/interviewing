def smallest_sum_path(arr):
    if arr is None:return 0
    if len(arr)==0 :

        dp=    [ [0] * (len(arr[0])+1) for i in range(len(arr)+1)]

    dp[0][0]=arr[0][0]

    for j in range(1,len(arr[0])):
        dp[0][j]=dp[0][j-1]+arr[0][j]
    for i in range(1, len(arr)):
        dp[i][0] = dp[i-1][0] + arr[i][0]
    for i in range(1,len(arr)):
        for j in range(1,len(arr[0])):
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])+arr[i][j]
    # print(dp)
    return dp[len(arr)-1][len(arr[0])-1]

if __name__ == '__main__':
    arr=[[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
    print(smallest_sum_path(arr))