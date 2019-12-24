''''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right'''

'''
注意处理边界问题！
就是在边界的退化情况下如果原grid的两条边上，如果扫描出现1故障点，那么对应的dp数组1故障点后的路就是0
然后，处理一般情况，和无障碍的情况类似，就是要判断是否出现1故障点即可。
'''

class Solution:
    def uniquePathsWithObstacles(self, grid):
        if not grid:
            return 0
        cnt = 0
        dp = [[ 0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        if grid[0][0] == 1:
            return cnt

        if 1 in grid[0]:
            tmp = grid[0].index(1)
            dp[0][:tmp] = [1] * tmp
        else:
            dp[0][:] = [1] * len(dp[0])

        for i in range(len(grid)):
            if grid[i][0] == 1:
                dp[:i][0] = [1] * i
                break
            dp[i][0] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if grid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    sc = Solution()
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    grid2 = [
        [0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ]

    grid3 = [
        [0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0,0]
    ]
    print(sc.uniquePathsWithObstacles(grid3))
