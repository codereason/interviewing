'''
2109. 向字符串添加空格
给你一个下标从 0 开始的字符串 s ，以及一个下标从 0 开始的整数数组 spaces 。

数组 spaces 描述原字符串中需要添加空格的下标。每个空格都应该插入到给定索引处的字符值 之前 。

例如，s = "EnjoyYourCoffee" 且 spaces = [5, 9] ，那么我们需要在 'Y' 和 'C' 之前添加空格，这两个字符分别位于下标 5 和下标 9 。因此，最终得到 "Enjoy Your Coffee" 。
请你添加空格，并返回修改后的字符串。

 

示例 1：

输入：s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
输出："Leetcode Helps Me Learn"
解释：
下标 8、13 和 15 对应 "LeetcodeHelpsMeLearn" 中加粗斜体字符。
接着在这些字符前添加空格。
示例 2：

输入：s = "icodeinpython", spaces = [1,5,7,9]
输出："i code in py thon"
解释：
下标 1、5、7 和 9 对应 "icodeinpython" 中加粗斜体字符。
接着在这些字符前添加空格。
示例 3：

输入：s = "spacing", spaces = [0,1,2,3,4,5,6]
输出：" s p a c i n g"
解释：
字符串的第一个字符前可以添加空格。

'''
class Solution:
    def addSpaces__TLE(self, s, spaces) :
        res = []
        j = 0
        for t in range(len(spaces)):
            space = spaces.pop(0)
            while j!=space:
                res.append(s[j])
                j+=1
            res.append(' ')
        res.append( s[space:])
        return ''.join(res)  ##超时

    
    def addSpaces(self, s, spaces) :
        i,j,t = 0,0,0
        res = ""
        len_s = len(spaces)
        while i<len(s) + len_s:
            if t< len(spaces):
                space = spaces[t]
                if j== space:
                    res += ' '
                    t+=1
                elif j!= space:
                    res+=s[j]
                    j+=1 #
            else:
                res+=s[space:]
                break
                
            i+=1
        return res

            


if __name__ == '__main__':
    solu = Solution()
    s = "icodeinpython"
    spaces = [1,5,7,9]
    print(solu.addSpaces(s,spaces))