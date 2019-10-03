
import sys
M_N= input().split(",")
grid = []
try:


    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

        a = list(map(int, line.split(',')))
        grid.append(a)

except:
    pass
# print(grid)
# grid = [[1,1,1,0,0],[0,0,1,0,0],[1,1,0,0,0],[1,0,0,0,0]]

# 4,5
# 1,1,1,0,0
# 0,0,1,0,0
# 1,1,0,0,0
# 1,0,0,0,0
map_res = {}
M,N = int(M_N[0]),int(M_N[1])
def solar_clusters(grid):
    res = 0


    for i in range(M):
        for j in range(N):
            if grid[i][j]==1:
                res+=1
                if res not in map_res:
                    map_res[res]=0
                    helper(i,j,M,N,grid,res)

    return res,map_res

def helper(i,j,M,N,grid,res):
    if i>=0 and j>=0 and i <M and j<N and grid[i][j]==1:
        grid[i][j]=2
        map_res[res]+=1
        helper(i-1,j,M,N,grid,res)
        helper(i +1, j, M, N, grid, res)
        helper(i , j-1, M, N, grid, res)
        helper(i , j+1, M, N, grid, res)

res,map_res_ = solar_clusters(grid)
if map_res_.keys() :
    print(max(map_res_.values()))
else:
    print(0)

