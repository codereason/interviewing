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

我们可以对上面的方法进行空间上的优化，由于最终的结果都是要乘到结果 res 中，所以可以不用单独的数组来保存乘积，而是直接累积到结果 res 中，我们先从前面遍历一遍，将乘积的累积存入结果 res 中，然后从后面开始遍历，用到一个临时变量 right，初始化为1，然后每次不断累积，最终得到正确结果，参见代码如下：

'''
class Solution2:
    '''
    Note: Please solve it without division and in O(n).


    '''
    def productExceptSelf(self, nums):
        if not nums :
            return None
        res= len(nums)*[1]
        for i in range(1,len(res)):
            res [i] = res[i-1] * nums[i-1]
        print(res)
        right = 1
        for i in range(len(res)):
            res[len(res)-i-1] = res[len(res) -1- i] * right
            right *= nums[len(res)-1-i]

        return res
if __name__ == '__main__':
    sc = Solution2()
    print(sc.productExceptSelf([1,2,3,4]))