'''
97. Interleaving String
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?


'''

##dp[i][j] 表示s1[0:i]和 s2[0:j] 满足成为 s3[0~i+j-1] 的 interleaving
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+ len(s2) != len(s3):
            return False
        
        dp = [(len(s2)+1)*[False] for _ in range(len(s1)+1)]
        
        dp[0][0] = True #表示s1[0:0] s2[0:0] 都是空字符串 
  
        for i in range(1,len(s1)+1):  #column
            dp[i][0] = True if s1[:i] == s3[:i] and dp[i-1][0] else False

        for i in range(1,len(s2)+1):
            dp[0][i] = True if s2[:i] == s3[:i] and dp[0][i-1] else False

        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                print(s3[:i+j])
                print(s1[i-1])
                print(s2[j-1])
                print(s3[:i+j-2])
                print("\n")
                ## 状态转移方程 见此图 https://pic.leetcode-cn.com/58e5041be1be0775a05ff0aadbbce04f82ee4d3eef673611a6adff8aefeac1f7.png
                if  (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False

        # print(dp)
        return dp[-1][-1]

if __name__ == '__main__':
    so = Solution()
    s1 = "ab"
    s2 = "c"
    s3 = "cab"
    print(so.isInterleave(s1,s2,s3))