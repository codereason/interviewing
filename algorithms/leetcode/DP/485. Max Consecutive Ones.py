'''
485. Max Consecutive Ones
Easy

346

299

Favorite

Share
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if (len(nums)==0):return 0
        if len(nums)==1:return 1 if nums[0]==1 else 0
        dp = (1+len(nums))*[0]
        dp[0]=1 if nums[0]==1 else 0
        for i in range(1,len(nums)):
            dp[i] = dp[i-1]+1 if nums[i]==1 else 0
        return max(dp)