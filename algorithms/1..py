
# print(len_)
# print(List)
len_ = input()

List=list(map(int,input().split(" ")))
# print(len_)
# print(List)
# min_ = float("inf")
# def fangcha(arr):
#     mean = sum(arr)/3
#     var_ = sum([(xi-mean)*(xi-mean)for xi in arr]) / 3
#     return var_
# from itertools import combinations
# a = combinations(List,3)
# print(a)
# for item in a:
#     print(item)
#     if min_ > fangcha(item):
#         min_ = fangcha(item)
# print(float('%.2f'%min_))
# for i in range(len(List)):
#     for j in range(i+1,len(List)):
#         for k in range(i+2,len(List)):
#             # print(fangcha([i,j,k]))
#             a =  fangcha([List[i],List[j],List[k]])
#             if min_>a:
#                 min_ =a
# print(float('%.2f'%min_))
# print(%.2fmin_)

# if __name__ == '__main__':
#     arr = [1,-1,0]
#     print(fangcha(arr))
List.sort()
min=float("inf")
