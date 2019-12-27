'''
18. 4Sum
Medium

1417

273

Add to List

Share
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
Accepted
283.3K
Submissions
882.6K
'''
'''
方法1，类似3sum里面的双指针发
'''

class Solution:
    def fourSum(self, nums, target):
        res = []
        if len(nums) < 4:
            return

        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return

        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l != r:
                    sums = nums[i] + nums[j] + nums[l] + nums[r]

                    temp = [nums[i], nums[j], nums[l], nums[r]]
                    # print(i,j,l,r)
                    if sums == target:
                        if temp[:] not in res:
                            res.append(temp)
                        while l+1 < r:
                            print("==")
                            if nums[l] == nums[l+1]:
                                l += 1
                            else:
                                break
                        # r -= 1
                        l+=1
                        # break
                    elif sums < target:
                        while l+1 < r:
                            print("<=")
                            if nums[l] == nums[l+1]:
                                l = l + 1
                            else:
                                break
                        l += 1
                    elif sums > target:
                        while l < r-1:
                            print(">=")

                            if nums[r] == nums[r-1]:
                                r -= 1
                            else:break
                        r -= 1
        return res

if __name__ == '__main__':
    sc = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    nums, target = [1,0,-1,0,-2,2,3,-3], 0
    # nums, target = [0,0,0,0], 0
    print(sc.fourSum(nums, target))
