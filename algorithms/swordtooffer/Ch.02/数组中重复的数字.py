def duplicate_1(nums):
    if (len(nums) > 1):
        nums.sort()
        replications = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] and nums[i] not in replications:
                replications.append(nums[i])
        return replications


def duplicate_2(nums):
    '''
    O(n)空间复杂度
    :param nums:
    :return:
    '''
    if len(nums) > 1:
        Dict = {}
        replications = []
        for i in range(len(nums)):
            if nums[i] not in Dict:
                Dict[nums[i]] = 1
            else:
                replications.append(nums[i])
        return replications


def duplicate_3(nums):
    '''
    链接：https://www.nowcoder.com/questionTerminal/623a5ac0ea5b4e5f95552655361ae0a8
来源：牛客网

此大法利用了哈希的特性，但不需要额外的存储空间。 因此时间复杂度为O(n)，不需要额外空间！

把当前序列当成是一个下标和下标对应值是相同的数组；
遍历数组，判断当前位的值和下标是否相等： 2.1. 若相等，则遍历下一位； 2.2. 若不等，则将当前位置i上的元素和a[i]位置上的元素比较：若它们相等，则成功！若不等，则将它们两交换。换完之后a[i]位置上的值和它的下标是对应的，但i位置上的元素和下标并不一定对应；重复2.2的操作，直到当前位置i的值也为i，将i向后移一位，再重复2.

前面的算法都没有很理想，理想的算法是时间复杂度为O(n)O(n)，空间复杂度为O(1)O(1)。注意到，数组中的数字都在0~n-1的范围内，所以，如果数组中没有重复的数，那么，当数组排序后，数字i将出现在下标为i的位置。由于数组中有重复的数字，有些位置可能存在多个数字，同时，有些位置可能没有数字。所以，我们可以利用这个思路高效解决这个问题。现在我们重排这个数组，从头到尾扫描每个数字，当扫描到下标为i的数字时，首先比较这个数字(记为m)是不是等于i。如果是，则接着扫描下一个数字；如果不是，则再拿它和第m个数字进行比较。如果它和第m个数字相等，就找到了一个重复的数字（该数字在下标为i和m的位置都出现了）；如果它和第m个数字不相等，就把第i个数字和第m个数字交换，把m放到属于它的位置。接下来再重复这个比较、交换的过程。下面则为该思路的Java实现程序：
---------------------
作者：yz930618
来源：CSDN
原文：https://blog.csdn.net/yz930618/article/details/76028770?utm_source=copy
版权声明：本文为博主原创文章，转载请附上博文链接！
    :param nums:
    :return:
    '''
    if len(nums) > 1:
        replications = []
        for i in range(len(nums)):
            while nums[i] != i:
                m = nums[i]
                if nums[i] == nums[m]:
                    replications.append(nums[i])
                    return


                nums[i],nums[m] = nums[m],nums[i]
        return replications


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    # nums = [1,2,2]
    # print(duplicate_1(nums))
    # print(duplicate_2(nums))
    print(duplicate_3(nums))
