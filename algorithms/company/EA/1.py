import sys
letter = []
try:


    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

        a = list(map(int, line.split(' ')))
        letter.append(a)

except:
    pass
import bisect
num,env = letter[0][0],letter[1:]
# print(num,env)
# print(env)

res = []
for _,h in sorted(env,key=lambda  x:(x[0],-x[1])):
    pos = bisect.bisect_left(res,h)
    if pos==len(res):
        res.append(h)
    else:
        res[pos]=h

print((len(res)+1)%1000000007)