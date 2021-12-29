'''
208. 实现 Trie (前缀树)
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
 

提示：

1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次
通过次数161,280提交次数224,391
'''
## 树节点  ##array 存储数据的 Version
class TrieNode():
    def __init__(self):
        self.data = 26*[None]
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode() 

        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if self.root.data[ord(word[0])-ord('a')] is None:
            self.root.data[ord(word[0])-ord('a')] = TrieNode()
        node = self.root.data[ord(word[0])-ord('a')]
        for i in range(1, len(word)):
            if  node.data[ord(word[i])-ord('a')] is None:
                node.data[ord(word[i])-ord('a')] = TrieNode()
            node = node.data[ord(word[i])-ord('a')]
        node.is_end = True

            
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if self.root.data[ord(word[0])-ord('a')] is None:
            return False
        node = self.root.data[ord(word[0])-ord('a')]
        for i in range(1,len(word)):
            if  node.data[ord(word[i])-ord('a')] is None:
                return False
            node = node.data[ord(word[i])-ord('a')]
        
        if node.is_end == True: 
            return True
        return False



    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if self.root.data[ord(prefix[0])-ord('a')] is None:
            return False
        node = self.root.data[ord(prefix[0])-ord('a')]
        for i in range(1,len(prefix)):
            if  node.data[ord(prefix[i])-ord('a')] is None:
                return False
            node = node.data[ord(prefix[i])-ord('a')] 
        return True
     

word = "abcdef"
obj = Trie()
obj.insert(word)
print(obj)
param_2 = obj.search("abcdef")
print(param_2)
prefix= "abcde"
param_3 = obj.startsWith(prefix)
print(param_3)
