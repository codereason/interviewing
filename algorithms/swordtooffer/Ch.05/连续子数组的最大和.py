# -*- coding:utf-8 -*-
class Solution:

    def FindGreatestSumOfSubArray(self, array):
        # write code here
        curMax = array[0]
        curSum = array[0]
        for num in array[1:]:
            if curSum < 0:
                curSum = num
            else:
                curSum += num
            if curSum > curMax:
                curMax = curSum

        return curMax


def sum_array(list):
    '''
    在任何讲动态规范的地方都能找到求最大连续子序列和的例子。具体来说，假设数组为a[i]，因为最大连续的子序列和必须是在位置0-(n-1)之间的某个位置结束。那么，当循环遍历到第i个位置时，如果其前面的连续子序列和小于等于0，那么以位置i结尾的最大连续子序列和就是第i个位置的值即a[i]。如果其前面的连续子序列和大于0，则以位置i结尾的最大连续子序列和为b[i] = max{ b[i-1]+a[i]，a[i]}，其中b[i]就是指最大连续子序列的和。
---------------------
作者：bitcarmanlee
来源：CSDN
原文：https://blog.csdn.net/bitcarmanlee/article/details/51526010
版权声明：本文为博主原创文章，转载请附上博文链接！
    :param list:
    :return:
    '''
    ans = len(list) * [0]
    if len(list) == 1: return list[0]
    if list[0] > 0:
        ans[0] = list[0]
        max_ = ans[0]
    for i in range(0, len(list)):
        if i == 0:
            ans[i] = list[i]
        else:
            ans[i] = ans[i - 1] + list[i] if ans[i - 1] + list[i] > list[i] else list[i]

    return max(ans)




if __name__ == '__main__':
    # list=[-1,-2,3,10,-4,7,2,-5]
    list=[-1,2]
    # print(Solution().FindGreatestSumOfSubArray(list))
    print(sum_array(list))