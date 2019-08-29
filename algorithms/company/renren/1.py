h = list(map(int, input().split()))
x = h[0]
N = h[1]
aaa = h[2:]

def f(arr):
    N = len(arr)
    res = []
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            if (i >> j) % 2 == 1:
                combo.append(arr[j])

        res.append(combo)

    return res


if sum(h[2:]) <= x:
    print(-1)
elif sum(h[2:]) >= 3 * x:
    print(-1)

else:

    res = f(aaa)
    min__ = []
    for item in res:
        if sum(item) >= x and sum(item) <= 3 * x:
            min__.append(sum(item))

    print(min(min__))
