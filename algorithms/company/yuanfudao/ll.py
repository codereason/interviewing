import sys
kkk = []
cov = []
try:
    line = sys.stdin.readline().strip()
    C = int(line)
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

        a = list(map(int, line.split(' ')))
        kkk.append(a)

except:
    pass
'''
4
3 1 1 1 
3 2 2 3
4 3 3 3 99


5
3 1 1 1 
3 2 2 3
5 2 3 33 55 99
5 0 2 3 4 99
6 99 99 99 99 99 99


'''

# print(C,kkk)

def fff2(arr):
    count = 0
    arr.sort()


    if len(arr)<3:
        return 0
    res = []
    for i in range(len(arr)-2):
        tmp = arr[i:i+2]
        # print(tmp)
        aaa = min(tmp)
        res.append(aaa)
    # print(res)
    count = max(res)
    arr2 = []
    for item in arr:
        if item-count==0:
            arr2.append(item)
        if item -count <0:
            arr2.append(item)
        if item-count>0:
            arr2.append(item-count)
        # else
    return count+fff2(arr2)

for item in kkk:
    print(fff2(item[1:]))