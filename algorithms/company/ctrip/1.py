s = str(input())
dist = []
i = 0
while i <len(s):
    tmp = s[i]
    index = s.rfind(tmp)
    dist.append(index-i+1)
    i = index+1

print(dist)


