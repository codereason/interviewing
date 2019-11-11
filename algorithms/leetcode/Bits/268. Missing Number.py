'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        return int(((length)*(length+1))/2) - sum(nums)

#其他方法 xor index和nums[index]
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tmp = len(nums)
        for i in range(len(nums)):
            tmp = tmp^nums[i]
            tmp = tmp^i

        return tmp

if __name__ == '__main__':
    so = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print(so.missingNumber2(nums))