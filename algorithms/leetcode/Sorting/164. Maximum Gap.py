'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
         (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
'''

'''
in linear time/space.
'''


class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        return self.biggestDiff(nums)

    def biggestDiff(self, A):
        if len(A) <= 1: return 0

        arr_min, arr_max = min(A), max(A)
        if (arr_min == arr_max): return 0
        maxs = [None] * (len(A) + 1)
        mins = [None] * (len(A) + 1)
        hasNum = [None] * (len(A) + 1)

        bid = 0
        for i in range(len(A)):
            bid = int(
                self.getBucket(A[i], len(A), arr_min, arr_max))  # 确定当前数 属于几号桶
            # print(A[i], "桶为：", bid)
            maxs[bid] = max(maxs[bid], A[i]) if hasNum[bid] else A[i]
            mins[bid] = min(mins[bid], A[i]) if hasNum[bid] else A[i]

            hasNum[bid] = True

        res = 0
        lastMax = maxs[0]
        for i in range(1, len(maxs)):
            if (hasNum[i]):
                res = max(res, mins[i] - lastMax)
                lastMax = maxs[i]
        return res
        # return biggestdiff

    def getBucket(self, num, length, min, max):  # 确定当前数 属于几号桶

        return ((num - min) * (length)) / (max - min)


'''
in O(nlogn).
'''


class Solution2:
    def maximumGap(self, nums):
        """
        :type nums: List[int]sss
        :rtype: int
        """
        nums.sort()
        max_value = 0
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if max_value < diff:
                max_value = diff

        return max_value
