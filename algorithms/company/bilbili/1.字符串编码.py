a = input()
length = len(a)
if length==0:
    print(0)


def dppp(s):
    m = {}
    def helper_function(s):
        if s is None:
            return 0
        elif len(s)==0:
            return 1
        elif s[0]=="0":
            return 0
        elif len(s)==1:
            return 1
        elif s in m:
            return m[s]
        else:
            result = helper_function(s[1:])
            if len(s)>=2 and int(s[0:2])<=26:
                result+=helper_function(s[2:])
            m[s] = result
        return  result
    return helper_function(s)

print(dppp(a))