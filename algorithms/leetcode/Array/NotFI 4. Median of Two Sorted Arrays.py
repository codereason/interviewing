'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2,nums1)

        l, r = 0 ,len(nums1)
        mid = ( len(nums1)+len(nums2)  +  1 ) // 2
        while l < r :
            m1 = l + (r-l)//2 #对nums1 进行二分法
            m2 = mid - m1
            if (nums1[m1] < nums2[m2-1]):
                l= m1 +1
            else:
                r = m1

        #分界一侧有空集的情况
  ##不够多
        i = l
        j = mid - i

        num1_left_max = nums1[i-1]



    def findMedianSortedArrays2(self, nums1,nums2) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
        else:
            return nums1[len(nums1) // 2]


if __name__ == '__main__':
    sc = Solution()
    nums1, nums2 = [1,3,4,5,6,7,8], [2,3,4,56,78]
    nums1, nums2 =[1,2],[3]
    print(sc.findMedianSortedArrays(nums1,nums2))
    print(sc.findMedianSortedArrays2(nums1, nums2))