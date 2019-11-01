'''
11. Container With Most Water
Medium

4179

485

Favorite

Share
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.





The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
双指针法, 水桶的面积用min(height[l], height[r])*(r-l)求得, 难点在于如何移动两个指针, 由于两个指针往中间移的时候, 宽度会降低, 我们需要找到更高的高度来求得结果, 水桶的高度是由较短的边决定的, 那么我们舍弃较短边, 如果较短边是左边, 那么左指针往右移, 寻找更大的高度, 如果较短边是右边, 那么右指针往左移.
Time: O(n/2)
Space: O(1)
————————————————
版权声明：本文为CSDN博主「闲庭信步的空间」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/danspace1/article/details/86643731


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        max_water = 0
        while l < r:
            temp_area = (r - l) * (min(height[l], height[r]))
            if max_water < temp_area:
                max_water = temp_area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water
