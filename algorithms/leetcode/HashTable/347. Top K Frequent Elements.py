'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Dict = {}
        for i in range(len(nums)):
            if nums[i] not in Dict:
                Dict[nums[i]] = 1
            else:
                Dict[nums[i]] += 1
        list = sorted(Dict, key=Dict.get, reverse=True)[:k]
        return list
        # print(list)
        # return [item[0] for item in list]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, ]
    k = 2
    print(Solution().topKFrequent(nums, k))
