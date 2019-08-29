num = int(input())
h = list(map(int,input().split()))





a = sum([pow(2,x) for x in h])
# print(a)

def f(x):
    if x&(x-1)==0:
        # print(x)
        return 1
    dp = (1+x)*[float("inf")]
    dp[0] = 0
    dp[1] = 1
    dp [2] = 1
    dp [3] = 2
    dp [4]=1
    for i in range(5,x+1):
        if i%2==1:
            dp[i] = dp[i-1] + 1
        else:
            t = 1
            # ss = pow(2,t)
            if i&(i-1)==0:
                dp[i]=1
            else:
                while i-pow(2,t)>=0:
                    ss = pow(2,t)

                    dp[i] = min(dp[i],dp[ss]+dp[i-ss])


                    t+=1

    return dp[-1]

print(f(a))