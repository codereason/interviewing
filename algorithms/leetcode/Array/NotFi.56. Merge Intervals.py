'''
56. Merge Intervals
Medium

2739

217

Favorite

Share
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


class Solution:
    def __init__(self):
        self.res = []

    def is_gap(self, list1, list2):
        if list1[0] <= list2[0] <= list1[1]:
            return True

        return False

    def merge_two(self, list1, list2):
        # [1,3],[2,5]
        if list1[1] == list2[0]:
            return [list1[0], list2[1]]

        if list2[1] == list1[0]:
            return [list2[0], list1[1]]

        if self.is_gap(list1, list2):
            return [min(list1[0], list2[0]), max(list1[1], list2[1])]

        return [list1,list2]

    def merge(self, intervals) :
        length = len(intervals)
        if length == 2:
            return self.merge_two(intervals[0], intervals[1])

        left = self.merge(intervals[:length // 2])
        right = self.merge(intervals[length // 2:])
        if len(left)
        return self.merge(left+right)

if __name__ == '__main__':
    so = Solution()
    arr =  [[1,3],[2,6],[8,10],[15,18]]
    ans = so.merge(arr)
    print(ans)