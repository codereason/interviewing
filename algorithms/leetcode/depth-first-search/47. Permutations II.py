'''
47. Permutations II
Medium

961

43

Favorite

Share
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution:
    def permute(self, nums):
        self.res=[]
        if len(nums)==0:return []
        nums.sort()
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
    print(s.permute([1,1,3]))