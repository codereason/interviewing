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





if __name__ == '__main__':
    list=[1,-2,3,10,-4,7,2,-5]
    print(Solution().FindGreatestSumOfSubArray(list))