import sys
data = []
while True:
    line = sys.stdin.readline().strip("\n")
    if line:
        data.append(line)
    else:
        break
'''
2
1 1 1 1
10
2 2 1 1
10 8
'''
T = data[0]
for i in range((len(data)-1)//2):
    n = int((data[2*i+1].split(" ")[0]))
    m = int((data[2*i+1].split(" ")[1]))
    x = int((data[2*i+1].split(" ")[2]))
    y = int((data[2*i+1].split(" ")[3]))
    v = [int(_) for _ in (data[2*i+2].split(" "))]
    clean_min=0
    clean_times=[]
    for i in range(n):
        clean_times.append(i*x+(n-i)*y)
    if n > 1 and y:
        ti = max(v)+y
    print(ti)