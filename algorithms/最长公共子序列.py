class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """

    def longestCommonSubsequence(self, str1, str2):
        List1 = list(str1)
        List2 = list(str2)
        if len(str1) == 0 or len(str2) == 0: return 0
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
        return max_
if __name__ == '__main__':
    print(Solution().longestCommonSubsequence("1234567","2345687"))