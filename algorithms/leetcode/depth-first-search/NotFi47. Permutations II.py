class Solution:
    def permuteUnique(self, nums):
        self.res = []
        if not nums:
            return []
        nums.sort()
        visited = [0]*len(nums)
        def dfs(temp,nums):
            print(self.res,"res")
            if len(temp[:]) == len(nums) :
                if temp not in self.res:
                    self.res.append(temp[:])
            else:
                for i in range(len(nums)):
                    if nums[i] in temp or nums[i] == nums[i - 1]:
                        continue
                    temp.append(nums[i])
                    print("temp", temp,"i", i)
                    dfs(temp,nums)
                    temp.pop()
        dfs([],nums)
        return self.res

if __name__ == '__main__':
    s=Solution()
    print(s.permuteUnique([1,2,1]))