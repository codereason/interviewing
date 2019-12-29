class Solution:
    def permuteUnique(self, nums):
        self.res = []
        if not nums:
            return []
        nums.sort()
        def dfs(temp,nums):
            print(self.res)
            if len(temp[:]) == len(nums) :
                if temp not in self.res:
                    self.res.append(temp[:])

            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs(temp,nums)
                temp.pop()
        dfs([],nums)
        return self.res

if __name__ == '__main__':
    s=Solution()
    print(s.permuteUnique([1,2,1]))