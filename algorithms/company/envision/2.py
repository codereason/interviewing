
List = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]  # 有三个岛

# 遍历所有的点，遇到1感染这些1区域，把1全部改为2，岛的数量+1；
# 遍历剩下的非2区域，继续这样做
print(len(List[0]))

res_map = {}

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    res = 0
    M = len(grid)
    if M > 0:
        N = len(grid[0])

        # print
        for i in range(M):
            for j in range(N):
                if grid[i][j] is "1" and res not in res_map:
                    res += 1
                    res_map[res]=1
                    self.infect(i, j, M, N, grid,res)

    return res

def infect( i, j, M, N, grid,res):
    if i >= 0 and j >= 0 and i < M and j < N and grid[i][j] == '1':
        grid[i][j] = '2'
        res_map[res]+=1
        infect(i - 1, j, M, N, grid)
        infect(i + 1, j, M, N, grid)
        infect(i, j - 1, M, N, grid)
        infect(i, j + 1, M, N, grid)


