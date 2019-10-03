import sys
s1,s2,s3,s4=[],[],[],[]
try:


    for item in [s1,s2,s3,s4]:
        for i in range(4):
            line = sys.stdin.readline().strip()
            if line == '':
                break

            a = list(map(float, line.split(',')))
            item.append(a)

except:
    pass

# print(s1,s2,s3,s4)

import math
def confirm_ver_vecs(l):
    s1 = [l[1][0]-l[0][0],l[1][1]-l[0][1]]
    s2 = [l[2][0] - l[1][0], l[2][1] - l[1][1]]
    s3 = [l[3][0] - l[2][0], l[3][1] - l[2][1]]
    s4 = [l[0][0] - l[3][0], l[0][1] - l[3][1]]
    a1 = s1[0]*s2[0]+s1[1]*s2[1]
    a2 = s2[0] * s3[0] + s2[1] * s3[1]
    a3 = s3[0] * s4[0] + s3[1] * s4[1]
    a4 = s4[0] * s1[0] + s4[1] * s1[1]
    if int(a1) == 0:
        return (s1,s2)
    if int(a2) == 0:
        return (s2, s3)
    if int(a3) == 0:
        return s3, s4
    if int(a4) == 0:
        return (s4, s1)


def getlength(x):
    return math.sqrt(x[0]**2+x[1]**2)
l1,l2 = confirm_ver_vecs(s1,)
l3,l4=confirm_ver_vecs(s2,)
l5,l6=confirm_ver_vecs(s3,)
l7,l8=confirm_ver_vecs(s4,)

dist = [l1,l2,l3,l4,l5,l6,l7,l8]


def panduanpingxing(l1,l2):
    if int(l1[0])==0 and int(l2[0])==0:
        return True
    elif int(l1[0])==0 or int(l2[0])==0:
        return False
    else:
        if int(l2[1]*l1[0]-l2[0]*l1[1])==0:
            return True
    return False
aaa ={}
res = []
for i in range(len(dist)):
    for j in range(i,len(dist)):
        if panduanpingxing(dist[i],dist[j]):
            if int(getlength(dist[i])+getlength(dist[j])) in res:

                aaa[int(getlength(dist[i])+getlength(dist[j]))] +=1
            else:
                aaa[int(getlength(dist[i]) + getlength(dist[j]))]=1
            if aaa[int(getlength(dist[i])+getlength(dist[j]))]==2:
                res.append(int(getlength(dist[i])+getlength(dist[j])))

print(res)