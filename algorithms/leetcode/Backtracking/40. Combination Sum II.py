'''
40. Combination Sum II
Medium

1240

52

Add to List

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
Accepted
271,252
Submissions
606,669
'''
class Solution:
    def combinationSum2(self, nums, target):
        if not nums or sum(nums) < target:
            return []
        self.res = []
        nums.sort()

        def dfs(nums, temp, target, index):

            if target == 0 and sorted(temp[:]) not in self.res:

                self.res.append(sorted(temp[:]))
                return

            elif target < 0:
                return

            for i in range(index, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp , target - nums[i], i + 1)
                temp.pop()

        dfs(nums, [], target, 0)

        return self.res

class Solution2:
    def combinationSum2(self, nums, target):
        if not nums:
            return []
        self.res = []
        nums.sort()

        def dfs(nums, temp, target, index):

            if target == 0:

                self.res.append(temp[:])
                return

            elif target < 0:
                return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                dfs(nums, temp , target - nums[i], i + 1)
                temp.pop()

        dfs(nums, [], target, 0)

        return self.res


if __name__ == "__main__":
    nums = [2,5,2,1,2]
    # nums = [2, 3, 5]
    target = 6
    # target = 5
    nums = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    sc = Solution2()
    print(sc.combinationSum2(nums=nums, target=target))
    import random
    random.randint(1,5)
