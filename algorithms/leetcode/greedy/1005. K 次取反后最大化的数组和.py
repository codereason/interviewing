'''
1005. K 次取反后最大化的数组和
给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：

选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
重复这个过程恰好 k 次。可以多次选择同一个下标 i 。

以这种方式修改数组后，返回数组 可能的最大和 。

 

示例 1：

输入：nums = [4,2,3], k = 1
输出：5
解释：选择下标 1 ，nums 变为 [4,-2,3] 。
示例 2：

输入：nums = [3,-1,0,2], k = 3
输出：6
解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
示例 3：

输入：nums = [2,-3,-1,5,-4], k = 2
输出：13
解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
 

提示：

1 <= nums.length <= 104
-100 <= nums[i] <= 100
1 <= k <= 104
通过次数34,968提交次数66,021
'''
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if k<=0:
                break
            if nums[i] < 0:
                nums[i] = -nums[i]
                k-=1
        if k%2 == 1: 
            # finding the smallest in the array
            min_num = nums[0]
            j = 0
            for i in range(1,len(nums)):
                if nums[i] < min_num:
                    min_num = nums[i]
                    j=i
            nums[j] = -nums[j]

            
        return sum(nums)
        # // 如果k没剩，那说明能转的负数都转正了，已经是最大和，返回sum
        # // 如果k有剩，说明负数已经全部转正，所以如果k还剩偶数个就自己抵消掉，不用删减，如果k还剩奇数个就减掉2倍最小正数。
if __name__ == "__main__":
    so = Solution()
    nums =   [4,2,3]
    k =1
    print(so.largestSumAfterKNegations(nums,k))