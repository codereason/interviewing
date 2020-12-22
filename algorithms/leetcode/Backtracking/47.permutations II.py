class Solution:
    '''
1） 要先排序，不然没法知道是不是重复元素出来了。
2） if (visited[i]) continue; 这行还是适用，因为这里i=0…nums.size()-1，所以两个2的visited[]不一样！！！
3）去重的关键在于下面者一行
if (i > 0 && (nums[i] == nums[i-1]) && !visited[i - 1]) continue;
**如果nums[i]==nums[i-1]但nums[i-1]又没有被visited过，说明后面的2要被排在前面的2前面了，这种情况要绝对避免，**所以continue。
4） 与Subset II区别。组合类重复元素去重的条件是：
if ((i!=index) && (nums[i-1]==nums[i])) //去重
continue;
上面没用到visited，但有i!=index。
    '''
    def backtrack(self, nums, used, tmp, result):
        if len(tmp) == len(nums) :
            
            self.res.append(tmp.copy())
            return
        for i in range(len(nums)):
            if i>0 and not used[i-1] and nums[i] == nums[i-1]:
                
                continue
            if used[i]: 
                continue

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