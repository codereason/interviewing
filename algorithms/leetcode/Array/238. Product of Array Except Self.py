'''
238. Product of Array Except Self
Medium

3315

281

Add to List

Share
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution:
    '''
    Note: Please solve it without division and in O(n).


    '''
    def productExceptSelf(self, nums):
        if not nums :
            return None
        left ,right ,res= len(nums)*[1], len(nums)*[1],len(nums)*[1]
        for i in range(1,len(left)):
            left [i] = left[i-1] * nums[i-1]
        for i in range(1,len(right)):
            right[len(right)-i - 1] = right[len(right) - i] * nums[len(right) - i]
        print(left)
        print(right)
        for  i in range(len(nums)):
            res[i] = left[i] * right[i]
        return res
'''Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

if __name__ == '__main__':
    sc = Solution()
    print(sc.productExceptSelf([1,2,3,4]))