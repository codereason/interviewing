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

if __name__ == '__main__':
    s="pwwkew"
    print(Solution().lengthOfLongestSubstring(s))

