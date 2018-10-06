'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''

'''
一种方法是使用字典哈希
'''
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        Dict = {

        }
        for i in range(len(nums)):
            if nums[i] not in Dict:
                Dict[nums[i]] = 1
            elif nums[i] in Dict:
                Dict[nums[i]]+=1
        return max(Dict,key=Dict.get)


# 另一种方法是直接对数组排序，返回数组中间的那个数一定是大多数值
class Solution2:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return ((nums[len(nums) // 2]))

