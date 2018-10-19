import re
def replaceSpaces(s):
    return s.replace(" ","%20")

def replaceSpaces2(s):
    lst = list(s)
    for item in lst:
        if item == ' ':
            lst[lst.index(item)]="%20"
    print(lst)
    return ''.join(lst)

if __name__ == '__main__':
    s = "we are young"
    print(replaceSpaces2(s))