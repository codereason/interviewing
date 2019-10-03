a = input()
N = int(a.split(";")[1])
ll = a.split(";")[0]
ll = list(map(int,ll.split(",")))
ll.sort(reverse=True)
# print(aa)
even=[]
odd=[]
for item in ll:
    if item%2==0:
        even.append(item)
    else:
        odd.append(item)

even = even[:N]
odd = odd[:N]
res = []
count = 0

# print(even,odd)
if len(even)<N:
    print(even+odd[:N-len(even)])

if len(even)==N:
    print(even)

if len(even)>N:
    print(even[:N])