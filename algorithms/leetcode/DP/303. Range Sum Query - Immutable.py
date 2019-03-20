'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
'''DP1'''
class NumArray2(object):

    def __init__(self, nums):
        self.dp = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.dp[i+1] = self.dp[i]+nums[i]

    def sumRange(self, i, j):
        return self.dp[j+1] - self.dp[i]



'''
我的解法，但是有一个例子TLE
'''''


class NumArray3:

    def __init__(self, nums):

        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        if i == j:
            return self.nums[i]
        if j == 0:
            return self.nums[j]
        return self.nums[j] + self.sumRange(i, j - 1)