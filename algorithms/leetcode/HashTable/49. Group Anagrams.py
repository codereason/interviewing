'''
49. Group Anagrams
Medium

2169

134

Favorite

Share
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}
        res = []

        if not strs:
            return res

        for i in strs:
            key = ''.join(sorted(list(i)))
            if key in dict_:
                dict_[key].append(i)

            else:
                dict_[key] = [i]

        for i in dict_:
            res.append(dict_[i])

        return res