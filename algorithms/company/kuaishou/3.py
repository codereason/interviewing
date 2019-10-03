M_N = input()
a_list = list(map(int,input().split(" ")))
b_list = list(map(int,input().split(" ")))
tmp = {}


# print(tmp)

total = 0
for i in range(len(a_list)):

    start_point = a_list[i]  #dianshu
    start_mark = b_list[i]
    for j in range(i+2,len(a_list),2):

        # print(i,j)
        # if i+2*j < len(a_list):
        if b_list[j] == start_mark and (j -i)%2==0:
            # print(start_point,start_mark,a_list[i+2*j])
            # print((start_point+a_list[i+2*j])*((i+1)+(i+2*j+1)))
            # print(i,j)
            total+=(start_point+a_list[j])*((i+1)+(j+1))



print(total)