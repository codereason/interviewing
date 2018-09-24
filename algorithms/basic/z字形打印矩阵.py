class Solution:
    def printMatZ(self, mat):
        flag = True
        x_i, x_j, y_i, y_j = 0, 0, 0, 0
        endx, endy = len(mat[0]) - 1, len(mat) - 1
        print(endx, endy)
        while (endy != x_j):
            self.printDiagLine(mat, x_i, x_j, y_i, y_j, flag)

            # if x_i!=endx: x_i+=1
            # if x_j!=endy and x_i==endx :x_j+=1
            # if y_j!=
            # x_i+=1 if x_i!=endx
            # print(x_i,x_j,y_i,y_j)
            if x_i != endx and x_j == 0:
                x_i = x_i + 1
            elif x_j != endy and x_i == endx:
                x_j = x_j + 1
            if y_i == 0 and y_j != endy:
                y_j = y_j + 1
            elif y_j == endy and y_i != endx:
                y_i = y_i + 1
            flag = not flag
        print(x_i, x_j, y_i, y_j)
        self.printDiagLine(mat, x_i, x_j, y_i, y_j, flag)

    def printDiagLine(self, mat, x_i, x_j, y_i, y_j, flag):

        if flag:
            while(x_j != y_j + 1):
                print(mat[x_j][x_i])
                x_j += 1
                x
        else:
            for _ in range(x_i, -1, y_i - 1):
                print(mat[x_i - _][_])


if __name__ == "__main__":
    mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19], [1, 2, 3, 4, 5]]
    Solution().printMatZ(mat)

    # print(len(mat[0]))
