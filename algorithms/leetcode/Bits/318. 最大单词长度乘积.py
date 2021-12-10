'''
318. 最大单词长度乘积
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

 

示例 1:

输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "xtfn"。
示例 2:

输入: ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。
示例 3:

输入: ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。
 

提示：

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] 仅包含小写字母
'''
class Solution(object):
    def maxProduct____TLE(self, words): #超时解法
        """
        :type words: List[str]
        :rtype: int
        """
        max_ = 0 #
        
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                list1 = 26*[0]
                list2 = 26*[0]
                a = words[i]
                b = words[j]
                # build bits array 
                for t in range(len(a)):
                    list1[ord(a[t])-ord('a')]+=1
                for t in range(len(b)):
                    list2[ord(b[t])-ord('a')]+=1
                if self.is_lap_lists(list1,list2):
                    max_ = max(max_,len(a)*len(b))
        return max_
    def is_lap_lists(self,list1,list2):
        for i in range(26):
            if list1[i] >0 and list2[i]>0:  # has same char
                return False 
        return True


class Solution2(object):
    def maxProduct(self, words): #位运算解法
        max_ = 0 #
        masks = [0]*len(words)
        for i in range(len(words)):
            for char in words[i]:
                print(char)
                print(bin(masks[i]))
                print(bin((1 << (ord(char) - ord('a')))))
                masks[i] = masks[i] | (1 << (ord(char) - ord('a')))

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                a = words[i]
                b = words[j]
                if masks[i]&masks[j] == 0:
                    max_ = max(max_,len(a)*len(b))
        return max_
if __name__ == '__main__':
    so = Solution2()
    print(so.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))