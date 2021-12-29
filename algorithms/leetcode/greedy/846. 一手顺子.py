'''
846. 一手顺子
Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。

给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。

 

示例 1：

输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
输出：true
解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
示例 2：

输入：hand = [1,2,3,4,5], groupSize = 4
输出：false
解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。
 

提示：

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
 

注意：此题目与 1296 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

通过次数12,880提交次数23,797
'''
##先统计次数，再模拟发牌
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize !=0:
            return False
        hand.sort() 
        import collections
        map = collections.defaultdict(int)
        for i in range(len(hand)):
            map[hand[i]]  += 1   
        i = 0
        lst = list(map.keys())
        while i < len(lst) :
            tmp = [lst[i]] 
            map[lst[i]]  -= 1   
            count = 1  
            while count < groupSize:
                if i+count < len(lst):
                    if map[lst[i+count]] > 0 and lst[i+count] -1 == tmp [-1]:
                        map[lst[i+count]] -= 1
                        tmp.append(lst[i+count])
                        count+=1  
                    else:
                        return False                  
                else:
                    break
            not_empty_flag = True
            for u in range(len(lst)):
                if map[lst[u]] > 0:
                    i = u
                    not_empty_flag = False
                    break
            if len(tmp) < groupSize:
                return False     
            if not_empty_flag:
                return True         
        return True




solu = Solution()
hand = [8,6,5,7,9]  
groupSize = 5
print(solu.isNStraightHand(hand,groupSize))


