import sys
arr = []
try:
    while True:
        line = sys.stdin.readline().strip()
        if line =='':
            break
        a = int(line)
        arr.append(a)
except:
    pass

arr = arr[1:]
print(arr)
res = []
for item in arr :
    if item < 0:
        res.append(item)

for item in arr :
    if item > 0:
        res.append(item)
# res.append(item for item in arr if item>0)
# print(res)
print(" ".join(str(item) for item in res))
