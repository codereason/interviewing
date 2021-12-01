'''
1446. 连续字符
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

请你返回字符串的能量。

 

示例 1：

输入：s = "leetcode"
输出：2
解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
示例 2：

输入：s = "abbcccddddeeeeedcba"
输出：5
解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。
示例 3：

输入：s = "triplepillooooow"
输出：5
示例 4：

输入：s = "hooraaaaaaaaaaay"
输出：11
示例 5：

输入：s = "tourist"
输出：1
 

提示：

1 <= s.length <= 500
s 只包含小写英文字母。
通过次数27,660提交次数45,357
'''
class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0 , 1  
        max_length = 1
        # if len(s) == 1: return 1
        while r < len(s):
            tmp = s[l:r]
            char = s[r]
            tmp_len = len(tmp)
            if char != tmp[-1]:
                l = r 

            else:
                tmp += s[r]
                tmp_len += 1
            r+=1 
            
            if max_length < tmp_len:
                max_length = tmp_len
        return max_length

if __name__ == '__main__':
    so = Solution()
    print(so.maxPower('leetcode'))