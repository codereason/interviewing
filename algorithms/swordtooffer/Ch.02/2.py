import sys
data = []
while True:
    line = sys.stdin.readline().strip("\n")
    if line:
        data.append(line)
    else:
        break

n = int(data[0])


lists=[]
for line in data[1:]:
    lists.append([int(_) for _ in line.split(',')])
itera = range(0,max([len(x) for x in lists]),n)
'''
3
2,5,6,7,9,5,7
1,7,4,3,4

4
2,5,6,7,9,5,7
1,7,4,3,4


'''

res=[]
for i in itera:
    for x in lists:
        res+=x[i:i+n]


print(','.join([str(x) for x in res]))