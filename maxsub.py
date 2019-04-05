
def FindGreatestSumOfSubArray(array):
    # write code here
    if len(array)==0:return 0
    if len(array)==1:return array[0]
    dp=(len(array)+1)*[-1]
    dp[0] = array[0]
    for i in range(1,len(array)):
        dp[i]=dp[i-1]+array[i] if array[i]>0 else 0
    return dp

if __name__ == '__main__':
    print(FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))