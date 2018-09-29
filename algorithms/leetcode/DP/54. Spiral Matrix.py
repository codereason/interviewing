'''
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        return self.circle_print(matrix)

    #     def printEdges(self,mat,i,j,k,l):
    #         # print(mat[0][1])


    #         return

    def circle_print(self, mat):
        List = []

        if mat == []: return []
        i, j, k, l = 0, 0, len(mat) - 1, len(mat[0]) - 1
        print(i,j,k,l)
        while (i <= k and j <= l):
            if (j == l):
                for _ in range(i, k + 1):
                    List.append(mat[_][l])
            elif (i == k):
                for _ in range(j, l + 1):
                    List.append(mat[i][_])

            else:
                cur_y = j
                while (cur_y < l):
                    List.append(mat[i][cur_y])
                    cur_y += 1

                cur_x = i
                while (cur_x < k):
                    List.append(mat[cur_x][l])
                    cur_x += 1
                cur_y = l
                while (cur_y > j):
                    List.append(mat[k][cur_y])
                    cur_y -= 1

                cur_x = k
                while (cur_x > i):
                    List.append(mat[cur_x][j])
                    cur_x -= 1

            i += 1
            j += 1
            k -= 1
            l -= 1

        print(List)
        return List


if __name__ == "__main__":
    mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    s = Solution()
    s.spiralOrder(mat)
