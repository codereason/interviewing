'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:return False
        flag = n&(n-1)
        #3二进制中，如果是2的幂次，那就是1000，100000这种，只有一个1
        return True if flag==0 else False