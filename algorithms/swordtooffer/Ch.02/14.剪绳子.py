def cut_rope(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    nums = [0]*(length+1)
    nums[0],nums[1],nums[2],nums[3]=0,1,2,3
    max_ = 0

    for i in range(4,length+1,1):
        for j in range(1,i//2 +1):
            if nums[i-j]*nums[j] > max_:
                max_ = nums[i-j]*nums[j]
        nums[i] = max_
    return nums[length]
# def cut_rope(n):
#     assert n>1
#     max_ = 0
#     for i in range(1,n):
#         max_ = max(max_,)
if __name__ == '__main__':
    print(cut_rope(10))