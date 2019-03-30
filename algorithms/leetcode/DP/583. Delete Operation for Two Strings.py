'''
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.

就是求最小公共子序列
'''

class Solution:
    def minDistance(self, str1: str, str2: str) -> int:
        List1 = list(str1)
        List2 = list(str2)
        # if len(str1) == 0 or len(str2) == 0: return 0
        dp = [[0] * (len(List2) + 1) for _ in range(len(List1) + 1)]
        # dp[0][0] = 1 if List1[0]==List2[0] else 0
        max_ = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if List1[i - 1] == List2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max([dp[i-1][j],dp[i][j-1]])
        for layer in dp:
            if max_ < max(layer):
                max_ = max(layer)
        # print(dp)
        return len(str1)-max_+len(str2)-max_