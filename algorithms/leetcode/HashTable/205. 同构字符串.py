'''
205. 同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 

示例 1:

输入：s = "egg", t = "add"
输出：true
示例 2：

输入：s = "foo", t = "bar"
输出：false
示例 3：

输入：s = "paper", t = "title"
输出：true
 

提示：

可以假设 s 和 t 长度相同。
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        map1, map2 = {} , {}
        for i in range(len(s)):
            if s[i] not in map1:
                map1[s[i]] = t[i]
            if t[i] not in map2:
                map2[t[i]] = s[i]
  
            if map1[s[i]] != t[i] or map2[t[i]]!=s[i]:
                return False
        return True

if __name__ == "__main__":
    so = Solution()
    s = "paper"
    t = "title"


    print(so.isIsomorphic(s,t))
