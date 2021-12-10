'''
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3,]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
 

提示：

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 

进阶：

如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
通过次数218,213提交次数458,642
'''
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = float("inf")  #
        l , r = 0, 1 
        tmp_sum = nums[l]
        tmp = nums[l:r]
        while r < len(nums):
            if tmp_sum < target:
                tmp_sum+=nums[r] 
                tmp.append(nums[r]) 
             
                if len(tmp[:]) < min_length and tmp_sum>= target :
                    min_length = len(tmp[:])        
            while tmp_sum>= target and l<=r:                
                min_length = min(len(tmp[:]),min_length)
                tmp.pop(0)
                tmp_sum -= nums[l]
                l+=1
            r+=1
        return min_length if min_length != float("inf")  else 0

if __name__ == "__main__":
    so = Solution()
    target = 7
    nums = [1,1,1,1,1,1,1,2,5]



    print(so.minSubArrayLen(target,nums))



