N = int(input())
import sys
arr = []
try:



    for i in range(N):
        arr.append(int(input()))

except:
    pass


if __name__ == '__main__':

    dp =[0]*1000000
    dp[0]=0
    dp[1]=0
    dp[2]=0
    dp[3]=0
    dp[4]=2
    x1,x2=0.5,2
    for i in range(5,100000):
        if i%4==1:
            dp[i]=dp[i-1]+x1
            x1+=1
        if i%4==2:
            dp[i] = dp[i - 2] + x2
            x2+=2
        if i%4==3:
            dp[i] = dp[i - 1] + x1

        if i%4==0:
            dp[i] = dp[i - 2] + x2





    for item in arr:
        for i in range(4,1000000):
            if  dp[i]>=item:
                print(i)
                break

