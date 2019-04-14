
import sys
res = []
N = int(input())
# print(list)
tmp=[0,1]
while True:
    if tmp[0]<=N<=tmp[1]:
        break
    tmp=[tmp[1],tmp[0]+tmp[1]]
print(min(abs(N-tmp[0]),abs(N-tmp[1])))