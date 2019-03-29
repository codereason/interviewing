'''

27 2 5 7  用最少的硬币数凑成27
'''

def least_coins(A,m):
    # 开辟数组，每个位子上表示该索引对应的价格能拼出的硬币个数
    f = (m+1)*[-1]   #状态数组
    n=len(A)
    f[0] = 0
    for i in range(1,m+1):
        f[i]=float("inf")
        for j in range(len(A)):
            if i > A[j] and f[i-A[j]]!=float("inf"):
                f[i] = min(f[i-A[j]]+1,f[i])


    if f[m]==float("inf"):return -1
    return f[m]



