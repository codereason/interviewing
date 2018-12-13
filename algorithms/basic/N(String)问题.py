'''
3(ab)=ababab
3(2(a))b=aaaaaab
解法，思路？？
感觉是将字符串分成1.最外面的括号体的左边，最外面的括号体，和括号体的右边
例如3(2(a))b 通过匹配，分为3，(2(a))，b（当然左右没有值的情况，要处理，例如左边没有值视为1
然后对里面的括号体递归操作
递归完了，就按照数字进行拼接操作
3(2(a))b -》3，(2(a))，b-》3，(a,a)，b->a,a,a,a,a,a,b
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
    import re
    re.compile()
    print(find_first_kuohao_neirong(s))