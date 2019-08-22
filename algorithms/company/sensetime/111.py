h= list(map(int,input().split()))
n,a,b,c,f0 =h[0],h[1],h[2],h[3],h[4]
def f(x):
    if x<0:return 0
    if x==0:return f0
    else:
        return a*f(x-1)+b*f(x-2)+c*f(x-3)+2*x*x-x+32767

print(f(n)%1000000007)