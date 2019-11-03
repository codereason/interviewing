'''
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        begin, end = nums[0], nums[-1]
        cnt = 0
        if begin == target:
            return 0
        if end == target:
            return len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            if nums[mid] < nums[r]:
                # 说明mid到r是有序的
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:  # target 在另一边，继续
                    r = mid - 1
            else:
                # 说明l 到mid 是有序的
                if target > nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    # target 在另一边，继续
                    l = mid + 1

        return -1


arr2 = [7, 0, 1, 2, 3, 4, 5, 6]
arr =[3,4,5,6,7,8,1,2]
target = 7

for tr in arr:
    print(search(arr,tr))

print(search(arr, target))
# print(search( arr2,7))
