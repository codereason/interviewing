
def FindGreatestSumOfSubArray(array):
    # write code here
    '''
    //若是相加之和一旦小于零，子数组从新开始，否则相加
    解体思路：

如果用函数f(i)表示以第i个数字结尾的子数组的最大和，那么我们需要求出max(f[0...n])。我们可以给出如下递归公式求f(i)

dp思想

这个公式的意义：

当以第(i-1)个数字为结尾的子数组中所有数字的和f(i-1)小于0时，如果把这个负数和第i个数相加，得到的结果反而不第i个数本身还要小，所以这种情况下最大子数组和是第i个数本身。

如果以第(i-1)个数字为结尾的子数组中所有数字的和f(i-1)大于0，与第i个数累加就得到了以第i个数结尾的子数组中所有数字的和

    '''
    if len(array)==0:return 0
    if len(array)==1:return array[0]
    dp=(len(array)+1)*[-1]
    dp[0] = array[0]
    for i in range(1,len(array)):
        dp[i]=dp[i-1]+array[i] if dp[i-1]>0 else array[i]
    return max(dp)

if __name__ == '__main__':
    print(FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))