'''
398. Random Pick Index
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.
 

Example 1:

Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
target is an integer from nums.
At most 104 calls will be made to pick.
通过次数15,685提交次数23,657
'''
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        self.array.sort()  
    def searchRange(self, nums,target) :
        if len(nums) == 1:
            return [0,0]
           
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
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ## 二分查找区间
        span = self.searchRange(self.array,target)
        import random        
        return random.randint(span[0],span[-1])

class Solution2(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ## 二分查找区间
        cand = []
        for i in range(len(self.array)):
            if self.array[i]==target:
                cand.append(i)
        import random        
        return random.choice(cand)


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
target = 3 
obj = Solution2(nums)
param_1 = obj.pick(target)
print(param_1)