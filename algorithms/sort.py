def q_sort(nums):
    if len(nums)<1:return  []
    if len(nums)>=1:
        pivot = nums[0]
        less,equal,more=[],[],[]
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num== pivot:
                equal.append(num)
            else:
                more.append(num)
        less = q_sort(less)
        more = q_sort(more)
        return less+equal+more

if __name__ == '__main__':
    nums=[4,5,3,1,5,7,123,53,463,23,12153]
    print(q_sort(nums))