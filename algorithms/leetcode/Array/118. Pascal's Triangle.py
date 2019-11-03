'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    def generate(self, numRows: int):
        res = []
        if numRows <= 0:
            res = []
            return res

        if numRows == 1:
            res = [[1]]
            return res
        if numRows == 2:
            res = [[1], [1, 1]]
            return res
        res = [[1], [1, 1]]
        for j in range(numRows - 2):
            temp = [1]
            for i in range(j + 1):
                temp.append(res[-1][i] + res[-1][i + 1])

            temp.append(1)
            # print(temp)
            res.append(temp)
        return res