'''
68. 文本左右对齐
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do",'yes','hell']
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''

class Solution:
    def fullJustify(self, words, maxWidth):

        #step1: check words
        def get_sequences(words,maxWidth):
          res = []
          tmp = ""
          i = 0
          while i < len(words):
            if tmp == "":
              tmp = words[i]
              i+=1
              if i ==len(words):
                res.append(tmp)
            else:
              if len(tmp + " "+ words[i]) <= maxWidth:
                tmp = tmp + " "+ words[i]
                i+=1
                if i== len(words):
                  res.append(tmp)
              else:
                res.append(tmp)
                tmp = words[i]
                i +=1
                if i== len(words):
                  res.append(tmp)
        
          return res
        def adjust_parentesis(str,maxWidth):
          num_words = len(str.split(" "))
          spaces = maxWidth - len(str) + num_words - 1  #待分配的空格数
          if num_words == 1: 
            res = [(maxWidth-len(str))*' ']
          else:
            per = spaces // (num_words - 1)
            res = (num_words - 1)*[per*' ']
            if spaces % (num_words - 1)!=0: 
              for i in range(len(res[:spaces % (num_words - 1)])): 
                res[i]+=' '
          return res
        
        res = get_sequences(words,maxWidth)
        for i in range(len(res[:])-1):
          res2 = adjust_parentesis(res[i],maxWidth)
          tmp = res[i].split(' ')
          tmp2 = ""
          for j in range(len(res2)):
            tmp2 += tmp[j] + res2[j]
          if len(tmp)!=1:
            tmp2 += tmp[-1]
          res[i] = tmp2  
        res[-1]+= (maxWidth-len(res[-1]))*' '
        return res

         


if __name__ == "__main__":
  solu = Solution()
  words=["aaaa","bb"]
  maxWidth = 20
  print(solu.fullJustify(words,maxWidth))