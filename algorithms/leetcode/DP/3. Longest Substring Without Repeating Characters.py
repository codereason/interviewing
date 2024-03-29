'''
3. Longest Substring Without Repeating Characters
Medium

5326

281

Favorite

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        '''
        一次遍历时，使用字典保存每个字符第一次出现的位置。这个方法我一直不知道叫什么名字，就勉强叫做prefix方法吧，因为需要维护已经遍历到的前缀部分。

当right向后遍历的过程中，如果这个字符在字典中，说明这个字符在前面出现过，即这个区间已经不是题目要求的不含重复字符的区间了，因此，需要移动left。

移动left到哪里呢？有个快速的方法，那就是移动到right字符在字典中出现的位置（即s[right]在前面的位置）的下一个位置。

无论如何都会使用right更新字典，另外记录最大区间长度即为所求。

注意，left更新的时候需要保留最大（最右）的位置。举例说明：

对于abba，当right指向最后的a的时候，left指向的是字典中保留的有第一个位置的a，如果不对此进行判断的话，left会移动到第一个字符b。

left一定是向右移动的，不可能撤回到已经移动过的位置。
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82022530
版权声明：本文为博主原创文章，转载请附上博文链接！
        :param s:
        :return:
        '''
        if not s:
            return 0
        left,right=0,0
        res = 0


        dict={}
        for right in range(len(s)):
            if s[right] in dict:
                left = max(left,dict[s[right]]+1)
            dict[s[right]]=right
            res = max(res,right-left+1)
        return res

    def lengthOfLongestSubstring2(self, s):
        '''
        所谓虫取法，就是根据某个条件交替移动前后指针，使得在双指针之内的这部分是满足题意要求的。

具体思路比较简单易懂，使用双指针，[left, right]双闭区间来保存子串的左右区间，对应着这个区间我们维护一个set，这个set里面全部是不重复的字符。

使用while循环，如果right字符不在set中，就让它进去；如果right在，就把left对应的字符给remove出去。

所以，当我们得到一个right位置的字符时，通过移动left和修改[left,right]区间内对应的的set，来保持了一个最小的不重复字符区间。这里需要注意的是，移动left的次数不一定就是1次，因为我们要保证left和right之间没有重复字符，而新添加的right字符出现的位置不一定刚刚就是left指向的位置。

比如：

a b c b b c b b
0 1 2 3 4 5 6 7

当right移动到3的时候字符时b，此时，set = {a, b, c}中，left=0，字符b在set中。

所以在while循环中反复移动left，当left移动到2的位置时，此时set = {c},字符b已经不在set中。

按照这个方式移动，set的个数最多的值即为最长子串。

一定注意：[left, right]区间和set是对应的，要同时维护。

下面的python代码是根据right指向的字符是否出现在set中而反复的进行循环，代码如下：

        :param s:
        :return:
        '''
        if not s:return 0
        left,right=0,0
        _ = set()
        res = 0
        while left < len(s) and right < len(s):
            if s[right] in _:
                if s[left] in _ :
                    _.remove(s[left])
                left+=1
            else:
                _.add(s[right])
                right+=1
                res = max(res,len(_))
        return res
class Solution2(object):
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
    s="pwwkew"
    print(Solution().lengthOfLongestSubstring(s))

