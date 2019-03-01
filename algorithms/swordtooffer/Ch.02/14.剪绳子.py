def cut_rope(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    nums = [0]*(length+1)
    nums[0],nums[1],nums[2],nums[3]=0,1,2,3
    max = 0

    for i in range(4,length+1,1):
        for j in range(1,i//2 +1):
            if nums[i-j]*nums[j] > max:
                max = nums[i-j]*nums[j]
        nums[i] = max
    return nums[length]

if __name__ == '__main__':
    print(cut_rope(10))