'''
46. Permutations

46. Permutations
Medium

1846

57

Favorite

Share
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    def permute(self, nums):
        self.res=[]
        if len(nums)==0:return []

        def dfs(nums,temp):
            if len(temp) == len(nums):
                self.res.append(temp[:])
            for i in range(len(nums)):
                if (nums[i]  in temp):
                    continue
                temp.append(nums[i])
                dfs(nums,temp)
                temp.pop()
        dfs(nums,[])
        return self.res


if __name__ == '__main__':
    s=Solution()
    print(s.permute([1,2,3]))