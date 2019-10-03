N = int(input())
arr = list(map(int,input().split(" ")))
ks = int(input())
res = []


def find_max_in_window(arr,ks):

    res = []
    import collections
    dequeue = collections.deque()
    for i,num in enumerate(arr):
        while dequeue and num>arr[dequeue[-1]]:
            dequeue.pop()
        dequeue.append(i)
        if i-dequeue[0]>=ks:
            dequeue.popleft()
        if i>= ks -1:
            res.append(arr[dequeue[0]])
    return res

res = find_max_in_window(arr,ks)
print(" ".join(str(item) for item in res))