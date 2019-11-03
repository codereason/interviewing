def search(nums, target):
    if not nums:
        return -1

    l, r = 0, len(nums) - 1
    begin, end = nums[0], nums[-1]
    cnt = 0
    if begin == target:
        return 0
    if end == target:
        return len(nums) - 1


    while l <= r:
        mid = (l + r) // 2



        if nums[mid] == target:
            return mid

        if nums[mid] < nums[r]:
            #说明mid到r是有序的
            if target > nums[mid] and target <= nums[r]:
                l =mid + 1
            else:#target 在另一边，继续
                r = mid - 1
        else:
            #说明l 到mid 是有序的
            if target > nums[l] and target <nums[mid]:
                r = mid - 1
            else:
                #target 在另一边，继续
                l = mid+1



    return -1
arr2 = [7,0,1,2,3,4,5,6]
arr = [3,4,5,6,7,8,0,1,2]
target =0
for target in arr:

    print (search(arr, target))
# print(search( arr2,7))