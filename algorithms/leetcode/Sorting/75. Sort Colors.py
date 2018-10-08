'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

方法：快排分区方法即可！
'''


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def partition(arr, pivot):
            if len(arr) > 1:
                less, more, cur = 0, len(arr) - 1, 0
                while (cur <= more):
                    if arr[cur] < pivot:
                        arr[less], arr[cur] = arr[cur], arr[less]
                        cur += 1
                        less += 1

                        continue
                    if arr[cur] == pivot:
                        cur += 1

                        continue
                    if arr[cur] > pivot:
                        arr[more], arr[cur] = arr[cur], arr[more]
                        more -= 1

                        continue

        partition(nums, 1)


class Solution_2:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def partition(arr):
            if arr == []:
                return
            i = 0
            j = len(arr) - 1
            k = 0
            while k <= j:  # 一开始用k<len(nums)出现了错误list index out of range
                if arr[k] == 0:
                    arr[k], arr[i] = arr[i], arr[k]
                    k += 1
                    i += 1
                elif arr[k] == 2:
                    arr[k], arr[j] = arr[j], arr[k]
                    j -= 1
                else:
                    k += 1

        partition(nums)
