import sys
kkk = []
try:
    ss = input()
    num = int(input())
    # line = sys.stdin.readline().strip()

    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

        a = int(line)
        kkk.append(a)

except:
    pass

# print(ss,num,kkk)


def howmany(s,b):
    count = 0
    for i in range(len(s)):
        for j in range(i):
            # print(s[j:i])
            if int(s[j:i])%1000000007==b:
                count+=1
    return count

for item in kkk:
    print(howmany(ss,item))
# print(howmany("1000000008001",8))
