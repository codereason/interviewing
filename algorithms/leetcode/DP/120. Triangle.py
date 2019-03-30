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

if __name__ == '__main__':
    arr = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Solution().minimumTotal(arr)
