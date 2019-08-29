def fff(arr):
    count = 0
    arr.sort()


    if len(arr)<3:
        return 0
    res = []
    for i in range(len(arr)-2):
        tmp = arr[i:i+2]
        # print(tmp)
        aaa = min(tmp)
        res.append(aaa)
    # print(res)
    count = max(res)
    arr2 = []
    for item in arr:
        if item-count==0:
            continue
        if item -count <0:
            arr2.append(item)
        if item-count>0:
            arr2.append(item-count)
        # else
    return count+fff(arr2)


def fff2(arr):
    count = 0
    arr.sort()


    if len(arr)<3:
        return 0
    res = []
    dict_ = {}
    for i in range(len(arr)-2):
        tmp = arr[i:i+2]
        # print(tmp)
        aaa = min(tmp)
        dict_[aaa] = tmp
        res.append(aaa)

    # print(res)
    count = max(res)
    duiyinglist = dict_[count]
    arr2 = []

    for item in arr:
        if item-count==0:
            arr2.append(item)
        if item -count <0:
            arr2.append(item)
        if item-count>0:
            arr2.append(item-count)
        # else
    return count+fff2(arr2)



arr = [99,99,99,99,99,99]
print(fff2(arr))