'''
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
 

提示：你可以假定该字符串只包含小写字母。

通过次数248,223提交次数460,565
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        import collections
        map = collections.defaultdict(int)
        for char in s:
            map[char]+=1 
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i 
        return res