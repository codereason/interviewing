# num = int(input())
h = list(map(int,input().split()))
length1,length2= len(h),len(h)


def max_sum(arr):
    xxx = []
    if len(arr)==1:

        return arr[0]
    if (len(arr)==2):
        xxx.append(max(arr[0],arr[1]))
        return max(arr[0],arr[1])
    count = 0
    xxx = []
    dp = len(arr) * [-1]
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    if arr[1]>arr[0]:
        xxx.append(arr[1])
    for i in range(2, len(arr)):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
        if dp[i - 2] + arr[i]>dp[i-1]:
            xxx.append(arr[i])

    min_value = float("-inf")
    # print(xxx)
    return max(dp)
res = []
flag = len(h)*[0]
def output(a,t):
    for i in range(t):
        if flag[i]:
            print(a[i])
            print("doe")
def lll(arr,n,t,h):
    if h==0:
        output(arr,t)
    else:
        if n == t:
            return
        else:
            flag[t]=True
            if h-arr[t]>=0:
                lll(arr,n,t+1,h-arr[t])
            flag[t]=False
            if h>=0:
                lll(arr,n,t+1,h)



max_ = max_sum(h)
lll(h,len(h),0,max_)
print(max_)
# print(res)
#背包

