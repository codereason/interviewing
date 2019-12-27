'''
遍历一遍数组，出现数字 - 1当做数组下标，将该下标在数组中的值存为负数，用来表示这个数字出现过。
例如，题目样例中的第一个数 4，就将数组下标为 4 - 1 = 3 的内容存为负数，即 nums[3] = nums[3] > 0 ? -nums[3] : nums[3]。然后再次遍历一遍数组，存储值为正数的数组下标 + 1，即为缺失的值。
还是拿题目样例来说明，按照上面的思路，要循环遍历两次。第一次遍历后数组内容变为:
————————————————
版权声明：本文为CSDN博主「扑街中的二娃」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Elliott_Yoho/article/details/53647960
'''
class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
        pass



