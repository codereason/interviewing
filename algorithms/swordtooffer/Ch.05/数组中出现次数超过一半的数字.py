def CountMoreThanHalf(list):
    digit,num =list[0], 1
    for i in list[1:]:
        if num==0:
            digit=i
            num=1
        elif i == digit:
            num+=1
        elif i != digit:
            num-=1
    return digit


if __name__ == '__main__':
    list=[1,2,2,2,3,4]
    print(CountMoreThanHalf(list))