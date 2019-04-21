'''
39. Combination Sum
Medium

1845

53

Favorite

Share
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
class Solution:
    def combinationSum(self, candidates,target):
        if len(candidates)==0:
            return[]
        self.res=[]
        candidates.sort()
        def dfs(candidates,temp,target,index):
            if target==0:
                self.res.append(temp[:])
                return
            # if target!=0 and len(temp)==len(candidates):
            #     temp=[]
            #     return
            for i in range(index,len(candidates)):
                if target<candidates[i]:
                    return
                temp.append(candidates[i])
                dfs(candidates,temp,target-candidates[i],i)
                temp.pop()

        dfs(candidates,[],target,0)

        return self.res

if __name__ == '__main__':
    s=Solution()
    print(s.combinationSum( [2,3,5],8))
