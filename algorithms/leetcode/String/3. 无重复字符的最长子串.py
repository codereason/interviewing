'''
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkewabcdj"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
通过次数1,342,864提交次数3,512,868
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 1 
        max_length = 0
        if len(s) == 1:return 1
        while r < len(s):
            tmp  = s[l:r]
            char = s[r] 

            if char in tmp :
                while char in tmp  :
                    l+=1
                    tmp = s[l:r]
                if tmp == "":
                    tmp = s[r]
            else: 
                tmp+= char
            r+=1
            if len(tmp) > max_length:
                max_length = len(tmp)
        return max_length


if __name__ == '__main__':
    so = Solution()
    print(so.lengthOfLongestSubstring("abcabcbbsda"))