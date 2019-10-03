h = list(map(int, input().split()))
k = int(input())
print(h,k)

res = []
for i in range(len(h)-k+1):
    res.append(sum(h[i:i+k])/k)

print(" ".join(str(format(item,'.2f')) for item in res))