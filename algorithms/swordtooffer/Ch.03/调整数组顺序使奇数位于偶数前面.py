def rotate_number(list):
    left,right = 0,len(list)-1
    while left != right:
        if is_even(list[left]) and not is_even(list[right]):
            list[left],list[right] = list[right],list[left]
            left+=1
            right-=1
        elif is_even(list[left]) and is_even(list[right]):
            right-=1
        elif not is_even(list[left]):
            left+=1
    return list

def is_even(num):
    return num % 2 == 0

def reOrderArray( array):
    # write code here
    odd,even = [],[]
    for i in array:
        odd.append(i) if i%2==1 else even.append(i)
    return odd+even
if __name__ == '__main__':
    list = [1,2,3,4,5,6]
    print(reOrderArray(list))