'''
1220. 统计元音字母序列的数目
给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：

字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
每个元音 'a' 后面都只能跟着 'e'
每个元音 'e' 后面只能跟着 'a' 或者是 'i'
每个元音 'i' 后面 不能 再跟着另一个 'i'
每个元音 'o' 后面只能跟着 'i' 或者是 'u'
每个元音 'u' 后面只能跟着 'a'
由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。

 

示例 1：

输入：n = 1
输出：5
解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
示例 2：

输入：n = 2
输出：10
解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
示例 3：

输入：n = 5
输出：68
 

提示：

1 <= n <= 2 * 10^4

'''
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9+7
        dp = [[0]*n for i in range(5)]
        for i in range(5):
            dp[i][0] = 1 
        
        # a 前面只能是e 和 u ,i
        # e 前面只能是a i
        # i 前面只能是 e o
        # o 前面 只能是 i 
        # u 前面 只能是o i
        
        for i in range(1,n):
            dp[0][i] = dp[1][i-1]+dp[2][i-1]+dp[4][i-1]   # a 前面只能是e 和 u ,i
            dp[1][i] = dp[0][i-1]+dp[2][i-1]  # e 前面只能是a i
            dp[2][i] = dp[1][i-1]+dp[3][i-1]  # i 前面只能是 e o
            dp[3][i] = dp[2][i-1]             # o 前面 只能是 i 
            dp[4][i] = dp[3][i-1] +dp[2][i-1]          # u 前面 只能是o i
        # print(dp)
        res = 0
        for i in range(5):
            res+=dp[i][-1]
        # print(res)
        return res%mod

class Solution2:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9+7
        dp = [1,1,1,1,1]

        
        # a 前面只能是e 和 u ,i
        # e 前面只能是a i
        # i 前面只能是 e o
        # o 前面 只能是 i 
        # u 前面 只能是o i
        
        for i in range(1,n):
            tmp1 = dp[1]+dp[2]+dp[4]  # a 前面只能是e 和 u ,i
            tmp2 = dp[0]+dp[2]  # e 前面只能是a i
            tmp3 = dp[1]+dp[3]  # i 前面只能是 e o
            tmp4 = dp[2]             # o 前面 只能是 i 
            tmp5 = dp[3] +dp[2]      # u 前面 只能是o i
            dp= [tmp1,tmp2,tmp3,tmp4,tmp5]
        # print(dp)
        
        # print(res)
        return sum(dp)%mod
##可以优化到O(N)复杂度




class Solution3:
    def countVowelPermutation(self, n: int) -> int:
        a = 1
        e = 1
        i = 1
        o = 1
        u = 1
        k = 1000000007
        for _ in range(1,n):
            tmp_a = e + i + u
            tmp_e = a + i
            tmp_i = e + o
            tmp_o = i
            tmp_u = i + o

            a = tmp_a % k
            e = tmp_e % k
            i = tmp_i % k
            o = tmp_o % k
            u = tmp_u % k

        return (a + e + i + o + u)% k

if __name__ == "__main__":
    solu = Solution()
    n =  2 * 10^4
    print(solu.countVowelPermutation(n))