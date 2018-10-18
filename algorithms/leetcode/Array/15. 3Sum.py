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
            if i > 0 and nums[i] == nums[i-1]:
                continue
                ###加一个判断 判断是否这个target数曾经出现过 如果出现过直接跳过去 可以省去时间避免TLE
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
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            s,e = i+1, N-1
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result
'''--------------------- 
作者：负雪明烛 
来源：CSDN 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/83115850 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
if __name__ == '__main__':
    nums = []
    print(Solution().threeSum(nums))
