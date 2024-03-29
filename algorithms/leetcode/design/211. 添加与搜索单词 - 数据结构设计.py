'''
211. 添加与搜索单词 - 数据结构设计
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：

WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
 

示例：

输入：
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
输出：
[null,null,null,null,false,true,true,true]

解释：
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

提示：

1 <= word.length <= 500
addWord 中的 word 由小写英文字母组成
search 中的 word 由 '.' 或小写英文字母组成
最多调用 50000 次 addWord 和 search
通过次数51,639提交次数101,034
'''
################################
## 这道题用前缀树比较好做
################################
class TrieNode():
    def __init__(self):
        self.data = 26*[None]
        self.is_end = False 



class WordDictionary(object):

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.node
        for i in range(len(word)):
            if cur.data[ord(word[i] )- ord('a')] == None:
                cur.data[ord(word[i] ) - ord('a')] = TrieNode()
            cur = cur.data[ord(word[i] ) - ord('a')]
        cur.is_end = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.node
        for i in range(len(word)):
            if word[i] == '.':   
                for  j in range(26):
                    if cur.data[j] != None:     
                        if self.search_only(cur.data[j], word[i+1:]  ):
                            return True
                return False
            else:
                if cur.data[ord(word[i] ) - ord('a')] == None:
                    return False
                else:
                    cur = cur.data[ord(word[i] )- ord('a')]
        return cur.is_end
                 
    #抽象出的 根据当前的节点和字符串头部 进行匹配搜索
    def search_only(self, cur, word):
        for i in range(len(word)):
            if word[i] == '.':   
                for  j in range(26):
                    if cur.data[j] != None:     
                        if self.search_only(cur.data[j], word[i+1:]   ):
                            return True
                return False
            else:
                if cur.data[ord(word[i] )- ord('a')] == None:
                    return False
                else:
                    cur = cur.data[ord(word[i] ) - ord('a')]
        return cur.is_end     


# Your WordDictionary object will be instantiated and called as such:
if __name__ == '__main__':
    word = "bad"
    obj = WordDictionary()
    obj.addWord(word)
    param_2 = obj.search("...")
    print(param_2)