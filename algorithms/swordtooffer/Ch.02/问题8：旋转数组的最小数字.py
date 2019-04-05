def least_number(nums):
    if len(nums)==1:return nums[0]
    if len(nums)==0:return None
    left,right=0,len(nums)-1
    while(nums[left]-nums[right]>=0):
        if right-left==1:
            return nums[right]
        mid = (left+right)//2
        if nums[mid]>=nums[left]:
            left=mid
        elif nums[mid]<=nums[left]:
            right=mid


if __name__ == '__main__':
    # nums=[3,4,5,1,2]
    nums=[1,2,3,4,5]
    print(least_number(nums))