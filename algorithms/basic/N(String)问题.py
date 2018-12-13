'''
3(ab)=ababab
3(2(a))b=aaaaaab
解法，思路？？
'''
def concat(s):
    count_left=0
    for item in s:
        if item == "(":
            count_left+=1
        # if item == ")":
        #     if count_left ==

def find_first_kuohao_neirong(s):
    return s.split("(")


if __name__ == '__main__':

    s = '3(2(a))'
    print(find_first_kuohao_neirong(s))