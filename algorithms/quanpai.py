import sys

arr = []
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        a = list(map(int, (line).split(' ')))
        arr.append(a)
except:
    pass


def quanpaiquchong(nums):
    res = []
    def back(nums_all,temp):
        if len(nums_all)==0 and temp not in res:
            res.append(temp)
            return
        for i in range(len(nums_all)):
            back(nums_all[:i]+nums_all[i+1:],temp+[nums_all[i]])
    t = []
    back(nums,t)

    return res
# print(q)
# set(quanpai([4,4,1,1,1]))
# print(quanpaiquchong([4,4,1,1,1]))
# def a
#
#5 5
4 4 1 1 1
4 3 0 1 2

#
# def anweixiangjia(list1, list2):
#
#         max = float("-inf")


# print("4 4 3 3 2")
def get_yushu(tem,m):
    return "".join(str(int(item)%m) for item in str(tem))


print(arr[0])
m ,n= arr[0][0],arr[0][1]
res1 = quanpaiquchong(arr[1])
print(res1)
res2 = quanpaiquchong(arr[2])
max_ = float("-inf")
for i in quanpaiquchong(arr[1]):
    for j in quanpaiquchong(arr[2]):
        temp1 = int("".join(str(item) for item in i))
        temp2 =int("".join(str(item) for item in j))
        mod1 = temp1+temp2
        mod2 = get_yushu(mod1,m)
        (max_,max_aaa) = (mod2,mod1) if int


print(max_)
