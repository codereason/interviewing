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
'''
会超时
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
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums.sort()
        res = []
        for t in range(N - 2):
            if t > 0 and nums[t] == nums[t - 1]:
                    continue
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if _sum == 0:
                    res.append([nums[t], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif _sum < 0:
                    i += 1
                else:
                    j -= 1
        return res
'''--------------------- 
作者：负雪明烛 
来源：CSDN 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/83115850 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
if __name__ == '__main__':
    nums = []
    print(Solution().threeSum(nums))
