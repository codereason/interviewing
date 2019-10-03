作者：james08
链接：https: // www.nowcoder.com / discuss / 253375?type = post & order = create & pos = & page = 1
来源：牛客网

第一题，给定不含重复但是元素相同数的序列A和B, 交换A中的元素使得A序列与B序列一样，移动的长度为 | i - j |，i, j为互换元素的位置。求最小移动。
例如：
4  # 长度
4
2
1
3
3
2
4
1
输出：
3
第一行1和3交换，然后3和4交换，总共3
暴力64 % 代码
1
2
3
4
5
6
7
8
9
10
11
12
13
14
n = int(input())
line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
res = 0
i = 1
while line1 != line2:
    for j in range(n):
        index = line2.index(line1[j])
        if abs(index - j) == i:
            line1[index], line1[j] = line1[j], line1[index]
            res += i
    i += 1

print(res)

第二题
画格子，1 * 1
的格子每次可以画一个对角线或者一个边，求画面积为N需要的最少次数
例如：
5  # 多少组数
1
2
3
4
5
输出：
4
4
6
6
7
找规律18 %
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
n = int(input())
line = []
for i in range(n):
    line.append(int(input()))
res = []
for i in range(len(line)):
    if line[i] == 1 or line[i] == 2:
        res.append(4)
    if line[i] == 3 or line[i] == 4:
        res.append(6)
    if line[i] > 4:
        if line[i] % 4 == 0:
            res.append(line[i])
        if line[i] % 2 == 0 and line[i] % 4 != 0:
            res.append(line[i] + 2)
        if line[i] % 2 == 1:
            res.append(line[i] + 2)
for i in res:
    print(i)
求大佬pythonAC代码
