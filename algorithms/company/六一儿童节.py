n=int(input())
h = list(map(int,input().split(" ")))
m = int(input())
w = list(map(int,input().split(" ")))

count=0
h.sort()
w.sort()
for i in w:
    for j in h:
        if i>=j:
            count+=1
            break
print(count)
'''
3
2 2 3
2
3 2
'''