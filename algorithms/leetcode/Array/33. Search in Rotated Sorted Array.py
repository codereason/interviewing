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
'''
具体来说，假设数组是A，每次左边缘为l，右边缘为r，还有中间位置是m。在每次迭代中，分三种情况：

（1）如果target==A[m]，那么m就是我们要的结果，直接返回；
（2）如果A[m]<A[r]，那么说明从m到r一定是有序的（没有受到rotate的影响），那么我们只需要判断target是不是在m到r之间，如果是则把左边缘移到m+1，否则就target在另一半，即把右边缘移到m-1。
（3）如果A[m]>=A[r]，那么说明从l到m一定是有序的，同样只需要判断target是否在这个范围内，相应的移动边缘即可。

注意，由于这个题目要进行和边缘元素的判断，所以没有采取[l,r)的左闭右开区间，而是使用了[l, r]双闭区间。
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/79534213
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
