'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution:
    def minimumTotal(self, triangle):
        if triangle is None:
            return 0
        n = len(triangle)
        m = len(triangle[-1])
        dp = [[float("inf")] * (m) for _ in range(n)]

        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(0, i+1):
                if j==0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j-1], dp[i - 1][j]) + triangle[i][j]
                print(dp[i][j])
        print(dp)
        return min(dp[-1])