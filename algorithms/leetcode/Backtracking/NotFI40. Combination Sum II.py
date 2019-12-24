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

class ImprovedSolution:
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
    sc = ImprovedSolution()
    print(sc.combinationSum2(nums=nums, target=target))
