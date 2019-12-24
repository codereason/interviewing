'''
34. Find First and Last Position of Element in Sorted Array
Medium

2312

110

Add to List

Share
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Accepted
391.7K
Submissions
1.1M
'''

'''
方法：二分查找，不过是找一段区间。，如果mid落在target的区域的话，，
就循环伸展左右两边，找到区间的
最左和最右。
注意edge case即可，例如长度为1、长度为2的数组找区间

'''
class Solution:
    def searchRange(self, nums,target) :
        if not nums or target not in nums:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else :
                return [-1,-1]
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                #[5,7,7,7,7,8]  7
                start = mid
                end = mid
                while start - 1 != -1 and nums[start-1]==nums[start]:
                    start = start - 1
                    
                while end +1 != len(nums) and nums[end+1] == nums[end]:
                    
                    end = end + 1
                    
                # print(start,end)
                return [start,end]
            
            elif nums[mid] > target:
                #[5,7,7,7,7,8,9,9,9,9,9,9,9]  7
                r = mid - 1

            
            elif nums[mid] < target:
                #[5,7,7,7,7,8,9,9,9,9,9,9,9]  9
                l = mid + 1 
        return [-1,-1]

            
            
                
if __name__ == "__main__":
    
    sc = Solution()
    nums =[5,7,7,7,7,8,9,9,9,9,9,9,9] 
    #[5,7,7,7,7,8,9,9,9,9,9,9,9]  9
    #[5,7,7,7,7,8,9,9,9,9,9,9,9]  7
    target = 1


    nums2 = [1,]
    nums3,target = [1,4],4
    print(sc.searchRange(nums3,target))