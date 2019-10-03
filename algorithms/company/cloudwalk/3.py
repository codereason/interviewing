bb = str(input())
aa = str(input())

import sys
if aa==bb:
    print(1)
    sys.exit()

else:
    j=0
    for i in range(len(bb)):
        if bb[i]==aa[j]:
            j+=1
        if j==len(aa):
            print(1)
            sys.exit()
    print(0)

