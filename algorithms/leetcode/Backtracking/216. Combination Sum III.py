'''
216. Combination Sum III
Medium

792

44

Add to List

Share
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
Accepted
143,384
Submissions
265,861
'''


class Solution:
    def combinationSum3(self, k: int, n: int):
        self.res = []
        if n == 0:
            return [[0]]
        if n < 0:
            return []
        nums = list(range(1, n))
        def dfs(nums, target, temp, index):
            if target == 0 and len(temp[:]) == k:
                self.res.append(temp[:])
                return
            if target < 0:
                return
            for i in range(index, len(nums)):
                if nums[i] < 10:
                    temp.append(nums[i])
                    dfs(nums, target - nums[i], temp, i + 1)
                    temp.pop()
        dfs(nums, n, [], 0)
        return self.res

if __name__ == '__main__':
    sc = Solution()
    print(sc.combinationSum3(2,18))