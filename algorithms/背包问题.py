class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        dp = [[0] * (m + 1) for _ in range(len(A) + 1)]

        for i in range(1, len(A)+1):
            for j in range(0, m+1):

                dp[i][j]=dp[i-1][j]
                if j >= A[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - A[i-1]] + A[i-1])
        print(dp[len(A)][m])

    def backPack2(self,m,A):
        '''
        一维没看懂
        :param m:
        :param A:
        :return:
        '''
        dp = (m+1)*[0]
        for i in range(1,len(A)):
            for j in range(m,1,-1):
                if j>=A[i]:
                    dp[j]=max(dp[j],dp[j-A[i]]+A[i])
        print(max(dp))

if __name__ == '__main__':
    '''
    92. 背包问题
中文English
在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]

样例
样例 1:
	输入:  [3,4,8,5], backpack size=10
	输出:  9

样例 2:
	输入:  [2,3,5,7], backpack size=12
	输出:  12
	
挑战
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.

注意事项
你不可以将物品进行切割。
'''
    A = [3,4,8,5]
    # A=[2,3,5,7]
    m = 10
    Solution().backPack(m,A)