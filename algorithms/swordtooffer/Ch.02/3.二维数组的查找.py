def search_in_matrix(mat, target):
    if len(mat) != 0:
        cols, rows = len(mat[0]), len(mat)
        row, col = 0, cols - 1
        while (cols > col >= 0 and rows > row >= 0):
            print(row, col)
            if mat[row][col] == target:
                print("Find target at ",row, col)
                return True
            elif mat[row][col] < target:
                row += 1
            else:
                col -= 1
    return False


if __name__ == '__main__':
    # mat = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    target = 1
    mat = [[1],[3]]
    print(search_in_matrix(mat, target))

    # print(mat[0][1])
