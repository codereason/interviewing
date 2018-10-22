'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 
'''
'''
Approach 3: One-pass Hash Table
It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.
'''


class Solution:
    def twoSum(self, nums, target):
        '''
        K-V K放元素 V放那个元素的索引索引
        :param nums: 
        :param target: 
        :return: 
        '''
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                return map[complement], i
            else:
                map[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
