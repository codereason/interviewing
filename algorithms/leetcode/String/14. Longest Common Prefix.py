'''
14. Longest Common Prefix
Easy

1416

1354

Favorite

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        if "" in strs: return ""
        min_length = min([len(item) for item in strs])
        if min_length == 0:return ""
        nums_item = len(strs)
        res = ""
        for j in range(min_length):
            for i in range(nums_item-1):
                if strs[i][j]!=strs[i+1][j]:
                    return res
            res+=strs[0][j]
        return res