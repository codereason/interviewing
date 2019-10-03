arr = list(map(int,input().split(",")))
point = int(input())
import sys

if len(arr)==0:
    print(-1)
    sys.exit()

index = arr.index(point)

if 2*(index)+2<len(arr):
    tmp = arr[2*(index)+2]
    tmp_index = arr.index(arr[2*(index)+2])
    while 2*(tmp_index)+1<len(arr):
        tmp = arr[2 * (tmp_index) + 1]
        tmp_index = arr.index(tmp)
    print(arr[tmp_index])
    sys.exit()

else:
    if 2 * (index) + 2 > len(arr):
        print(-1)
        sys.exit()
