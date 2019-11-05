'''
258. Add Digits
Easy

535

874

Favorite

Share
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''
'''
根据提示，当输入从1到100变化时，可以发现，输出在“1，2，3，4，5，6，7，8，9，1，2，3，4，5，6，7，8，9，…”这样循环。于是，就有了下面O(1)的算法。
dr(n) = 0, if n = 0
dr(n) = 9, if n != 0 and n mod 9 == 0
dr(n) = n mod 9, if n mod 9 != 0
或，
dr(n) = 1 + (n-1) mod 9

这个问题又叫做“digit root”问题，参看：
https://en.wikipedia.org/wiki/Digital_root#Congruence_formula

代码一

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9
————————————————
版权声明：本文为CSDN博主「coder_orz」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/coder_orz/article/details/51378231
'''


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num)) == 1:
            return num
        nums = str(num)
        while len(nums) != 1:
            tmp = sum(map(int, list(nums)))
            print(tmp)
            nums = str(tmp)
            print(tmp)
        return int(nums)

if __name__ == '__main__':
    so = Solution()

    print(so.addDigits(66))