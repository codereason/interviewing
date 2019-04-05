def repeat_number(nums):
    dict={}
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]]=1
        else:return nums[i]