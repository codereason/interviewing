# ac

def sub(arr):
    arr.sort()
    arr = arr[::-1]
    left = arr[:1]
    right = arr[1:]
    sum_left = sum(left)
    sum_right = sum(right)
    for i in range(1,len(arr)-1):

        if sum_left >sum_right:
            left.sort()
            return left
        else:
            tmp = right[i-1]
            left.append(tmp)
            right.remove(tmp)
            print(left,right)
            sum_left+=tmp
            sum_right-=tmp
            print(sum_left,sum_right)




moves = [5,3,2,4,1,2]

print(sub(moves))

#第二题 优惠券  未ac

#第三题  gfg上的 ac

#第四题 好像是error digit 9>1  15/17

#第五题 是linux文件路劲  ac