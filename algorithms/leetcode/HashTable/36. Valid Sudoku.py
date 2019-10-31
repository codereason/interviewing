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
#
#
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#
#         # 判断行
#         for i in range(len(board)):
#             if self.hasDuplicate(board[i]):
#                 return False
#
#             ##判断列
#         for i in range(9):
#             list = []
#             for j in range(9):
#                 list.append(board[j][i])
#             if self.hasDuplicate(list):
#                 return False
#         ##判断9宫
#         list = []
#         rank1, rank2 = 0, 0
#         for count in range(9):
#             for i in range(3):
#
#                 for j in range(3):
#                     list.append(board[i + 3 * rank1][j + 3 * rank2])
#
#             if self.hasDuplicate(list):
#                 return False
#             rank1 += 1
#             if
#
#     def hasRowDuplicate(list):
#         dict = {}
#         for i in range(len(list)):
#             if list[i] != "," and list[i] not in dict:
#                 dict[list[i]] = 1
#             if list[i] in dict:
#                 dict[list[i]] += 1
#                 return True
#         return False


class Solution2:
    def isValidSudoku(self, board):
        if not board:
            return False

        def helper(arr):
            # 判断9个数(not ',')是否存在重复
            _ = {}
            for i in range(len(arr)):
                if arr[i] != '.':
                    if arr[i] in _:
                        return False
                    else:
                        _[arr[i]] = 1
            return True

        def is_row_valid(board):

            for line in board:
                if helper(line) is False:
                    # print(line)
                    # print("row invalid")
                    return False
            return True

        def is_col_valid(board):
            _ = []
            for i in range(9):
                for j in range(9):
                    _.append(board[j][i])
                if helper(_) is False:
                    # print(_)
                    # print("Column invalid")
                    return False
                else:
                    _ = []
            return True

        def is_3_3_valid(board):
            # index 3*3 array how to ?
            '''
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
            :param board:
            :return:
            '''
            _ = []
            i, = 0,
            while i <= 6:
                j = 0
                while j <= 6:
                    _ = [board[i][j], board[i + 1][j], board[i + 2][j],
                         board[i][j + 1], board[i + 1][j + 1], board[i + 2][j + 1],
                         board[i][j + 2], board[i + 1][j + 2], board[i + 2][j + 2]]
                    j += 3
                    # print(_)
                    if helper(_) is False:
                        # print(_)
                        # print("3*3 invalid")
                        return False

                i += 3
            return True
            # arr = [board[i*3:i*3 + 3] for j in range(3)]

        flag1, flag2, flag3 = is_row_valid(board), is_col_valid(board), is_3_3_valid(board)
        return flag1 and flag2 and flag3

if __name__ == '__main__':
    s = Solution2()
    arr =             [
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
    arr2 = [
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
    print(s.isValidSudoku(arr))
    print()
    print(s.isValidSudoku(arr2))