'''
90. Subsets II
Medium

1228

56

Add to List

Share
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Accepted
239,143
Submissions
535,830
'''
class Solution:
    def subsetsWithDup(self, nums) :
        self.res = []
        if not nums:
            return
        if nums == []:
            return [[]]
        nums.sort()
        def dfs(nums, temp, index):
            if temp not in self.res and temp!=[]:
                self.res.append(temp[:])
                # return
            # elif temp in self.res:
            #     return
            print(len(nums))
            for i in range(index, len(nums)):
                temp.append(nums[i])
                print( temp, nums[i])
                dfs(nums, temp, i+1)
                temp.pop()

        dfs(nums, [], 0)
        self.res.append([])
        return self.res

# if __name__ == '__main__':
#     sc = Solution()
#     nums = [1,2,2]
#     print(sc.subsetsWithDup(nums))

if __name__ == '__main__':
    sc = Solution()
    nums = [1,2,2]
    nums = []
    print(sc.subsetsWithDup(nums))