'''
和为s的两个数字，数组已经排好序
'''


class Solution:
    def FindNumbersWithSum(self, nums, s):
        # write code here
        if len(nums) < 2:
            return []
        left, right = 0, len(nums) - 1

        while left != right:
            if nums[left] + nums[right] < s:
                left += 1
            elif nums[left] + nums[right] > s:
                right -= 1
            elif nums[left] + nums[right] == s:
                return nums[left], nums[right]
        return []


'''
所有和为s的连续正数序列
'''


def continusSum(s):
    left, right = 1, 2
    mid = (s + 1) / 2
    list = []
    cur = left + right
    while left < mid:
        if cur==s:
            list.append(range(left,right+1))
        while cur > s and left<mid:

            cur = cur - left
            left += 1
            if cur==s:
                list.append(range(left, right + 1))
        big+=1
        cur+=big
    return list
