'''
172. Factorial Trailing Zeroes
Easy

615

867

Add to List

Share
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

所有的尾部的0可以看做都是2*5得来的，所以通过计算所有的因子中2和5的个数就可以知道尾部0的个数。实际上，2的个数肯定是足够的，所以只需计算5的个数即可。
要注意，25=5*5是有两个5的因子；125=5*5*5有3个5的因子。比如，计算135!末尾0的个数。
首先135/5 = 27，说明135以内有27个5的倍数；27/5=5，说明135以内有5个25的倍数；5/5=1，说明135以内有1个125的倍数。当然其中有重复计数，算下来135以内因子5的个数为27+5+1=33。


'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n = n//5
            res += n
        return res
