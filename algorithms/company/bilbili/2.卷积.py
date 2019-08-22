import sys
kkk = []
cov = []
try:
    line = sys.stdin.readline().strip()
    h, w = int(line.split(" ")[0]) , int(line.split(" ")[1])
    kkk.append([h,w])
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

        a = list(map(float, line.split(' ')))
        kkk.append(a)

except:
    pass

# print(kkk)
# print(kkk[1:h+1])
# print(int(kkk[h+1][0]))
# print(kkk[h+2:])
'''
3 3
40 24 135
200 239 238
90 34 94
2
0.0 0.6
0.1 0.3

'''

def conv(list1,list2):
    ##list1是图像 list2是卷积核
    res =[]
    m, n = len(list2),len(list2[0])
    y ,x = len(list1),len(list1[0])
    t = y - m +1
    r = x-m+1   #使用步数，即最后的形状
    res = [[0]*r for t in range(t) ]
    for i in range(t):
        for j in range(r):
            # tmp = list1[i:i+m,j:j+m]
            tmp = [list1[_][j:j+m] for _ in range(i,i+m)]  #数组切片
            res[i][j] =min(255,matttttt(tmp,list2))
    return res

def matttttt(mat1,mat2):  #两个相同尺寸的matrix 求内机和
    sum = 0
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            sum+=mat1[i][j]*mat2[i][j]
    return sum

result = conv(kkk[1:h+1],kkk[h+2:])
for item in result:
    print(" ".join([str(int(num)) for num in item]))
# print(result)
