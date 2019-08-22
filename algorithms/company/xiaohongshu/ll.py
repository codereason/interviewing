def max_sum(arr):
    # xxx = []
    # if len(arr)==1:
    #
    #     return arr[0],xxx
    # if (len(arr)==2):
    #     xxx.append(max(arr[0],arr[1]))
    #     return max(arr[0],arr[1]),xxx
    count = 0
    dp = len(arr)*[-1]
    dp[0]=arr[0]
    dp[1] = max(arr[0],arr[1])
    for i in range(2,len(arr)):
        dp[i]=max(dp[i-1],dp[i-2]+arr[i])
        if dp[i-2]+arr[i] >  dp[i-1]:
            count+=1

    min_value= float("-inf")
    return max(dp),count
    print(str(dianzanshu2)+" "+str(j) )
if __name__ == '__main__':
    arr = [10,4,5,7,2,3,4,6]
    print(max_sum(arr))