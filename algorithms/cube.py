def cal(grid):
    area = 0
    for i in range(len(grid)):
        grid[i].append(0)

    grid.append([0]*len(grid[0]))
    for i in range(len(grid)-1):
        for j in range(len(grid[0])-1):
            if grid[i][j]!=0:
                area+=2 +grid[i][j]*4 - min(grid[i][j], grid[i][j+1])*2 - min(grid[i][j],grid[i+1][j]) * 2
    return area
def surface(arr):
    area = 0
    for i ,row in enumerate(arr):
        for j,_ in enumerate(row):
            if _:
                area+= (6*_)-(2 *( _ - 1 ))
                if len(arr)>i+1:
                    area -= 2*min(arr[i+1][j],arr[i][j])
                if j+1<len(row):
                    area  = area - 2*min(row[j],row[j+1])
    return area
##接受很多行

import sys
arr = []
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        a = list(map(int, (line).split(' ')))
        arr.append(a)
except:
    pass
print(arr)
print(surface(arr[1:]))
