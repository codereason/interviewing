'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        """
        采用二分法
        """
        '''
        # mid = x // 2
        if x == 1: return 1
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2  # mid一定是整数
            if (x == mid ** 2) or ((mid + 1) ** 2 > x and mid ** 2 < x):
                return (mid)
            elif x > mid ** 2:
                left = mid
            else:
                right = mid

        return left

    def mySqrt2(self, x):
        import math
        return int (math.sqrt(x))