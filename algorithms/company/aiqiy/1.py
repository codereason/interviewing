# 给定一个长度为N-1且只包含0和1的序列A1到AN-1，如果一个1到N的排列P1到PN满足对于1≤i<N，当Ai=0时Pi<Pi+1，当Ai=1时Pi>Pi+1，则称该排列符合要求，那么有多少个符合要求的排列？
# #
# # 4
# # 1 1 0
# #
# # 3


N = int(input())
arr = list(map(int, input().split(" ")))

# print(N,arr)
# N=4
# arr=[1,1,0]

# import collections, itertools
#
# all = list(itertools.permutations([i for i in range(1, N + 1)]))
#
#
# # print(all)
# def compare(a1, a2, bit):
#     if bit == 1:
#         return a1 > a2
#     if bit == 0:
#         return a1 < a2
#
#
# def check_one(item):
#     count = 0
#
#     for i in range(len(item) - 1):
#         if not compare(item[i], item[i + 1], arr[i]):
#             return False
#
#     return True
#
#     # print(item)
#
#
# count = 0
# for item in all:
#     if check_one(item): count += 1
# print(count)
# dp = [1 for i in range(len(arr)+1)]
# tmp = [0 for i in range(len(arr)+1)]
# for i in range(1,len(arr)+1):
#     if arr[i-1]==1:
#         for j in range(i+1):
#             tmp[j]=sum(dp[j:i])
#     else:
#         for j in range(i+1):
#             tmp[j]=sum(dp[:j])
#
#     dp,tmp =tmp,dp
# print(sum(dp)%(10**9+7))
mod = 10**9+7
n=len(arr)+1
dp = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    dp[i][0]=1

a = 0
increase=0
decrease =len(arr)
for j in range(1,n):
    if arr[j-1]==0:
        increase+=1
        for i in range(increase,decrease+1):
            dp[i][j] = (dp[i-1][j]+dp[i-1][j-1])%mod
            a = dp[i][j]

    else:
        decrease-=1
        for i in range(decrease,increase-1,-1):
            dp[i][j]=(dp[i+1][j]+dp[i+1][j-1])%mod
            a=dp[i][j]

print(a)
