'''
16. 3Sum Closest
Medium

1513

112

Add to List

Share
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Accepted
407.3K
Submissions
891.1K
'''
'''
想要得到三个数字的和，要求这个和尽可能的靠近target，那么同样需要先排序，然后使用一个指针遍历，另外两个指针分别指向下一个元素和最后一个元素然后向中间靠拢的方式。在靠拢的过程中如果当前的和与target的差距比要返回的结果与target更小，那么更新要返回的结果。

指针的移动策略是如果和比目标值大，说明我们需要把这个和调小一点；如果和比目标小，那么需要把和调大一点。如果相等那么就返回结果。

时间复杂度是O(N^2)，空间复杂度是O(1)。
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/83116781

'''


class Solution:
    def threeSumClosest(self, nums ,target) -> int:

        if len(nums) < 3:
            return
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        cur_gap, closest_gap = 0, nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l != r:
                sums = (nums[i] + nums[l] + nums[r])
                if abs(sums - target) == 0:
                    return target

                if abs(sums - target) < abs(closest_gap - target):
                    closest_gap = sums
                #移动策略  比target小的话，应该把左指针右移动，使当前sum更大一点；反之，右指针左移动
                if sums < target:
                    l += 1

                else:

                    r -= 1

        return closest_gap

if __name__ == '__main__':
    sc = Solution()
    nums =  [-1, 2, 1, -4]
    target = 1
    print(sc.threeSumClosest(nums,target))