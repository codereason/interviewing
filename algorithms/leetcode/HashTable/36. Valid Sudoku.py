'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 判断行
        for i in range(len(board)):
            if self.hasDuplicate(board[i]):
                return False

            ##判断列
        for i in range(9):
            list = []
            for j in range(9):
                list.append(board[j][i])
            if self.hasDuplicate(list):
                return False
        ##判断9宫
        list = []
        rank1, rank2 = 0, 0
        for count in range(9):
            for i in range(3):

                for j in range(3):
                    list.append(board[i + 3 * rank1][j + 3 * rank2])

            if self.hasDuplicate(list):
                return False
            rank1 += 1
            if

    def hasRowDuplicate(list):
        dict = {}
        for i in range(len(list)):
            if list[i] != "," and list[i] not in dict:
                dict[list[i]] = 1
            if list[i] in dict:
                dict[list[i]] += 1
                return True
        return False
