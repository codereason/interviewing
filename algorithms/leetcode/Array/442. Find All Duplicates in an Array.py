'''
根据题目要求：给的验证数组最多出现两次相同的数，或者出现一次某个数，要求不开辟空间，时间复杂度是O(n).因为数组输入的特点 1<=sums[i]<=n,则可以把原数组当hash表用 ，因为原数组是正数，标为负数表示出现过，如果遇到负数 就表示第二次出现，就可以找出所有出现过2次的数
————————————————
版权声明：本文为CSDN博主「cndn_gfz」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/gfz19930128/article/details/53468926
'''
class Solution:
    def findDuplicates(self, nums):
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                res.append(abs(nums[i]))
            nums[abs(nums[i])-1] *=-1

        print (nums)
        # for i in range(len(nums)):
        #     if nums[nums[i]-1] > 0:
        #         res.append(i)
        return res

if __name__ == '__main__':
    sc = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(sc.findDuplicates(nums))