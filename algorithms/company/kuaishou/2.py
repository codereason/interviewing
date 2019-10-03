N = int(input())
import sys
schs = []
try:
    while True:
        line = sys.stdin.readline().strip()
        if line=="":
            break
        schs.append(list(map(int,line.split(" "))))
except:
    pass

print(schs)
def cal_gap(sc):
    for
    for item in sc:
        if item[1]- item[0] == 2: