class Solution:
    def backtrack(self, nums, used, tmp, result):
        if len(tmp) == len(nums) :
            
            self.res.append(tmp.copy())
            return
        for i in range(len(nums)):
            if not used[i-1] and nums[i] == nums[i-1]:
                continue
            if not used[i]:
                used[i] = True
                tmp.append(nums[i])
                self.backtrack(nums,used,tmp,self.res)
                tmp.pop()
                used[i] =False

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        used = [False for i in range(len(nums))]
        print(used)
        self.res = []
        self.backtrack(nums,used,[],self.res)
        return self.res

if __name__ == "__main__":
    nums = [1,2,3,4]
    sc = Solution()
    print(sc.permuteUnique(nums))