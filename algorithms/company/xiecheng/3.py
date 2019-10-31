N = float(input())
if N<0:
    N=-1*N
y=1.0
while(abs(y*y-N) > 1e-10):
    y=(y+N/y)/2
print("{:.4f}".format(y ))