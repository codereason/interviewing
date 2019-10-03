s = input()

dict_ = {}
# s = "aba"
x=[]


# print(x)
for item in s:
    if item not in dict_:
        dict_[item]=1
    else:
        dict_[item]+=1

print(dict_[max(dict_,key=dict_.get)])