List1=list(map(int,input().split(" ")))
List2=list(map(int,input().split(" ")))
L,N=List1[0],List1[1]
List2.sort()
#中国位数，两端？
sum1,sum2,sum3 = 0,0,0

sum1+=List2[0]
for i in range(1,len(List2)):
    sum1+=List2[i]- List2[i-1] -1
print(sum1)


sum2+=L - 1 - List2[-1]
for i in range(1,len(List2)):
    sum2+=List2[i]- List2[i-1] -1
print(sum2)

# if len(List2)%2!=0:


# print(min(sum1,sum2,sum3))
