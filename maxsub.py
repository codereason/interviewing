
def FindGreatestSumOfSubArray(array):
    # write code here
    '''
    //若是相加之和一旦小于零，子数组从新开始，否则相加

    '''
    if len(array)==0:return 0
    if len(array)==1:return array[0]
    dp=(len(array)+1)*[-1]
    dp[0] = array[0]
    for i in range(1,len(array)):
        dp[i]=dp[i-1]+array[i] if dp[i-1]>0 else array[i]
    return dp

if __name__ == '__main__':
    print(FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))