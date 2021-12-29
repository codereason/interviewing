'''
507. 完美数
对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。

给定一个 整数 n， 如果是完美数，返回 true，否则返回 false

 

示例 1：

输入：num = 28
输出：true
解释：28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 和 14 是 28 的所有正因子。
示例 2：

输入：num = 6
输出：true
示例 3：

输入：num = 496
输出：true
示例 4：

输入：num = 8128
输出：true
示例 5：

输入：num = 2
输出：false
'''
class Solution:
    def checkPerfectNumber(self, num: int):
        if n == 1: return False
        n = 2  
        import math 
        res = 0
        while n <= math.sqrt(num)  : 
            if num % n == 0: 
                print(num//n,n)
                res += num // n
                res += n
            n+=1
        
        if res+1 == num: return True 
        return False

# if __name__ == "__main__":
#     solution = Solution()
#     num =  2
#     n = 1
#     while n<= 10^8:
#         if solution.checkPerfectNumber(n):
#             print(n)
#         n+=1