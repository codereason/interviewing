import sys
N = int(input())
arr = []
try:
    while True:
        line = sys.stdin.readline().strip()
        if line =='':
            break
        a = list(map(int, line.split(' ')))
        arr.append(a)
except:
    pass

from collections import defaultdict

G = [[] for _ in range(N)]
degree = [0 for _ in range(N)]
for x,y in arr:
    G[y].append(x)
    degree[x]+=1

zero_degree = [i for i in range(N) if degree[i]==0]
if len(zero_degree)==0:
    print(True)
    sys.exit()

for i in zero_degree:
    for j in G[i]:
        degree[j] -=1
        if degree[j] == 0:
            zero_degree.append(j)

print(len(zero_degree)!=N)