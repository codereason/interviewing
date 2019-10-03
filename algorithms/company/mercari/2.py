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