'''
 Welcome to vivo !
'''

def solution(step_list):

    n,cur_max,next_max,steps = len(step_list),0,0,0
    for i in range(n):
        if i > cur_max:
            steps+=1
            cur_max=next_max
            if cur_max>=n : break
        next_max = max(next_max,step_list[i]+i)

    return steps

step_list = [int(i) for i in input().split()]
print(solution(step_list))