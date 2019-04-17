'''
121. Best Time to Buy and Sell Stock
Easy

2406

116

Favorite

Share
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Accepted


'''

'''
本解法其实199/200，有一个testcase超时了，但是是正确的
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        if len(prices)==1:
            return 0
        dp = [-1]*(len(prices)+1)
        dp[0]=0
        for i in range(1,len(prices)):
            dp[i]=max(dp[i-1],prices[i]-min(prices[:i]))
        return max(dp) if max(dp)>0 else 0