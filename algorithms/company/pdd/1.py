line = input()
line2 = input()
M,N = int(line.split(" ")[0]),int(line.split(" ")[1])
arr = list(map(int,line2.split(" ")))
arr.sort()

def help(arr,N,M):
    res = 0

    for i in range(N):
        res+=arr[i]*arr[N*2-i-1]
    return res

if N*2==M:
    print(help(arr,N,M))

else:
    print(help(arr, N, M))

