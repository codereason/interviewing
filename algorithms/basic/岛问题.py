'''
给定一个二维数组，所有位置的值不是0就是1。规定每个位置可以和它上下左右位置上的值相连。有一个叫做岛的概念，定义如下： 
连成一片的1，如果周围都是0，那么这一片1，构成一个岛。

求整张图上有多少个岛。

例如： 
0 0 0 0 0 0 0 0 0 
0 1 1 0 0 1 1 1 0 
0 1 1 1 0 0 0 1 0 
0 1 1 0 0 0 0 0 0 
0 0 0 0 0 1 1 0 0 
0 0 0 0 1 1 1 0 0 
0 0 0 0 0 0 0 0 0 
这张图上有三个岛。

0 0 0 0 0 0 0 0 0 
0 1 1 0 1 1 1 1 0 
0 1 1 1 1 0 0 1 0 
0 1 1 0 0 0 0 1 0 
0 0 0 0 0 1 1 1 0 
0 0 0 0 1 1 1 0 0 
0 0 0 0 0 0 0 0 0 
这张图上有一个岛。
1.针对二维数组中的元素进行逐次用BFS或DFS进行遍历，如果遇到边界或值为0的时候，就停下来，统计BFS或DFS的遍历次数即可
2.如果登岛的时候（当第一次遇见值为1的时候），就对周边的1进行感染，那么这个岛就会被一次感染完。如果遇到其他岛屿的话，如上操作。
那么我们可以根据几次感染的次数对岛屿的个数进行估计
---------------------

本文来自 Shwan_Ma 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/shwan_ma/article/details/76616192?utm_source=copy 

'''

List = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]  # 有三个岛

# 遍历所有的点，遇到1感染这些1区域，把1全部改为2，岛的数量+1；
# 遍历剩下的非2区域，继续这样做
print(len(List[0]))


class Solution:
    def numIslands(self, grid):
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
                    if grid[i][j] is "1":
                        res += 1
                        self.infect(i, j, M, N, grid)

        return res

    def infect(self, i, j, M, N, grid):
        if i >= 0 and j >= 0 and i < M and j < N and grid[i][j] == '1':
            grid[i][j] = '2'
            self.infect(i - 1, j, M, N, grid)
            self.infect(i + 1, j, M, N, grid)
            self.infect(i, j - 1, M, N, grid)
            self.infect(i, j + 1, M, N, grid)
