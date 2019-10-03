'''
Welcome to vivo !
'''


def solution(stone_list):
    # TODO Write your code here
    all_weights = sum(stone_list)
    avg = int(all_weights/2)

    dp =[[0]*(2000) for _ in range(300)]

    for i in range(1,len(stone_list)):
        for j in range(1,avg+1):
            dp[i][j] = dp[i-1][j]
            # print(j-stone_list[i])
            if j>= stone_list[i] :
                if dp[i][j]<dp[i-1][j-stone_list[i]]+stone_list[i]:
                    dp[i][j] =dp[i-1][j-stone_list[i]]+stone_list[i]

    return all_weights - dp[len(stone_list)][avg]*2


stone_list = [int(i) for i in input().split()]
print(solution(stone_list))