'''
179. 最大数
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

 

示例 1：

输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"
示例 3：

输入：nums = [1]
输出："1"
示例 4：

输入：nums = [10]
输出："10"
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 109
通过次数130,074提交次数317,568

'''

class Solution:
    def largestNumber(self, nums) -> str:
        nums = [str(n) for n in nums]
        nums.sort(key=str,reverse=True)
        print(nums)
        return ''.join(nums)

        def sorter(x, y):
            ##按照字典序排序，但是要注意3 和30 是3大
            if str(x)+str(y) > str():
                return -1
            if x < y:
                return 1
            return 0

if __name__ == "__main__":
    solu = Solution()
    nums = [3,30,34,5,9]
    print(solu.largestNumber(nums))