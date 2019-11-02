'''
79. Word Search
Medium

2374

126

Favorite

Share
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution:

    def __init__(self):
        self.flag = False

    def exist(self, board, word) -> bool:
        if not board:
            return False

        string = ""
        visited = [[0]*len(board[0]) for _ in range(len(board))]
        # flag = False
        _1,_2,_3,_4 = False,False,False,False,
        def dfs(string, word, i, j):
            if not word:
                return True
            if word[0]!=board[i][j]:
                visited[i][j] =1
                return False
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] is not word[0]:
                return False
            #     return False
            _1,_2,_3,_4 = False,False,False,False
            if j+1<len(board[0]):
                _1 = dfs(string + board[i][j + 1], word[1:][:], i, j + 1)
            if i+1<len(board):
                _2 = dfs(string + board[i + 1][j], word[1:][:], i + 1, j)

            if i-1 >=0 and i-1<len(board):
                _3 = dfs(string + board[i-1][j], word[1:][:], i - 1, j)

            if j-1>=0 and j-1 <len(board[0]):
                _4 = dfs(string + board[i][j-1], word[1:][:], i, j-1)
            return _1 or _2\
                   or _3   or _4

        for i in range(len(board)):
            for j in range(len(board[0])):
                flag = dfs(string, word, i, j)
                if flag == True:
                    return True
        return False

if __name__ == '__main__':
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCB"
    so = Solution()
    print(so.exist(board,word))

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not str:
            return False

        m = len(board)
        n = 0
        if board[0]:
            n = len(board[0])

        word_len = len(word)

        def _dfs(x, y, word_index):
            if word_index == word_len:
                return True

            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[word_index]:
                return False

            board[x][y] = '0'
            #up
            if _dfs(x-1, y, word_index+1):
                return True
            #down
            if _dfs(x+1, y, word_index+1):
                return True
            #left
            if _dfs(x, y-1, word_index+1):
                return True
            #right
            if _dfs(x, y+1, word_index+1):
                return True
            board[x][y] = word[word_index]

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if _dfs(i, j, 0):
                        return True
        return False
