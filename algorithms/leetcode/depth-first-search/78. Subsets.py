'''
78. Subsets
Medium

1768

46

Favorite

Share
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []


        def dfs( nums, temp, i, ):
            self.res.append(temp[:])
            for j in range(i,len(nums)):
                temp.append(nums[j])
                dfs(nums,temp,j+1)
                temp.pop()
        dfs(nums,[],0)
        return self.res




if __name__ == '__main__':
    s=Solution()
    print(s.subsets([1,2,3]))