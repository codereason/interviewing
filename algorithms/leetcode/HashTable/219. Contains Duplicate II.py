'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) > 1:
            Dict1 = {}  # 存放那个数出现的最早的索引

            for i in range(len(nums)):
                if nums[i] not in Dict1:
                    Dict1[nums[i]] = i

                else:

                    if abs(i - Dict1[nums[i]]) <= k:

                        return True
                    Dict1[nums[i]] = i



        return False


if __name__ == '__main__':
    nums = [2,2]
    k = 1
    print(Solution().containsNearbyDuplicate(nums, k))
