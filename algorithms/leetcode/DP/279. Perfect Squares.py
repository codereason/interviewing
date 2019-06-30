'''
279. Perfect Squares
Medium

1501

118

Favorite

Share
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
class Solution:
    '''
    本解法Python3超时，但是CPP同款解法却可以通过，服了
    '''
    def numSquares(self, n: int) -> int:
        if n <=0 :return None
        dp = (n+1)*[float("inf")]  ##dp[i]表示数字i的least number of perfect square numbers
        dp[0] = 0
        
        dp[1]=1
        for i in range(2,n+1):
            j = 1
            while(j*j<=i):
                dp[i] = min(dp[i-j*j]+1,dp[i])
                j+=1
        return dp[n]