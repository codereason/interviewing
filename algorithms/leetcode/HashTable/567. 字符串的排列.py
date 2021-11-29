'''
567. 字符串的排列
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

 

示例 1：

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
示例 2：

输入：s1= "ab" s2 = "eidboaoo"
输出：false
 

提示：

1 <= s1.length, s2.length <= 104
s1 和 s2 仅包含小写字母
通过次数131,318提交次数303,496
'''

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2)< len(s1):
            return False
        if len(s1) == len(s2):
            return self.check(s1, s2)

        len1,len2 = len(s1),len(s2) 
        for i in range(0,len2 - len1 + 1):
            if self.check(s1,s2[i:len1+i]):
                return True 
        return False

    def check(self, s1, s2):
        s1_list,s2_list = [0]*26, [0]*26
        for char in s1:
            s1_list[ord(char)-ord('a')] += 1

        for char in s2:
            s2_list[ord(char)-ord('a')] += 1
        return s1_list == s2_list

if __name__ == '__main__':
    so = Solution()
    print(so.checkInclusion("","eidboaoo"))