'''
96. Unique Binary Search Trees
Medium

1645

64

Favorite

Share
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class Solution:
    def numTrees(self, n):
        '''
        求解方法：动态规划


    假设DP(n)表示n个节点组成不同二叉搜索树的种类数，分别考虑1到n作为根结点的情况。

(1) 根节点为1，则左子树必定为空，右子树为2...n个节点，那么种类数为1*DP[n-1]，也可以表示为DP[0]*DP[n-1]。

(2) 根节点为2，则左子节点为1，右子树为3...n个节点，即DP[1]*DP[n-2]

(3) 根节点为3，则左子节点为1,2，右子树为4...n个节点，即DP[2]*DP[n-3]

......

每个根有DP[n-1]种情况， 根结点2到n-1时，每个根有DP[左边剩下数字] * DP[右边剩下数字] 种情况。

状态转移方程：DP(n) = DP(0)*DP(n-1)+DP(1)*DP(n-2)+...+DP(n-1)*DP(0)   注：下面代码可左右滑动查看
        :param n:
        :return:
        '''
        if n < 1: return 0
        if n == 1: return 1
        dp = (n + 1) * [0]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.numTrees(3)
