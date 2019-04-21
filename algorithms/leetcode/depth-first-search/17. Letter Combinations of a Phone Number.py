'''
17. Letter Combinations of a Phone Number
Medium

2034

281

Favorite

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''


class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        button = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = []
        self.dfs(0, digits, button, '', ans)
        return ans

    def dfs(self, i, digits, button, cur, ans):

        if i== len(digits):
            ans.append(cur)
            return
        for c in button[int(digits[i])]:

            self.dfs(i + 1, digits,button,cur + c, ans)
if __name__ == '__main__':
    s=Solution()
    print(s.letterCombinations("23"))