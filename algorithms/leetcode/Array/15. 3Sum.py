'''

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        # print(nums)
        for i in range(len(nums) - 2):

            left, right = i + 1, len(nums) - 1
            while (left < right):

                if nums[left] + nums[right] < -1 * nums[i]:
                    left += 1

                elif nums[left] + nums[right] > -1 * nums[i]:
                    right -= 1
                else:

                    tmp = [nums[i], nums[left], nums[right]]
                    # print(left, right, tmp)
                    if tmp not in res:
                        res.append(tmp)
                    left += 1
                    right -= 1
                    continue

        return res


if __name__ == '__main__':
    nums = []
    print(Solution().threeSum(nums))
