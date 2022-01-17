'''
500. 键盘行
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。
American keyboard

 

示例 1：

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
示例 2：

输入：words = ["omk"]
输出：[]
示例 3：

输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]
 

提示：

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] 由英文字母（小写和大写字母）组成
通过次数53,265提交次数71,559
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first =  {char.lower():1 for char in "qwertyuiop"}
        sec = {char.lower():1 for char in "asdfghjkl"}
        third = {char.lower():1 for char in "zxcvbnm"}
        print(first,sec,third)
        def checkString(string,map):
            for char in string:
                if char not in map:
                    return False
            return True
        res = []
        for word in words:
            if checkString(word.lower(),first) or checkString(word.lower(),sec) or checkString(word.lower(),third):
                res.append(word)
        return res
                                                                                                
  