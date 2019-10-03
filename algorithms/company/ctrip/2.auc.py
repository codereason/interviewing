N= int(input())
import sys
labels = []
y = []
try:

    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break

        h, w = int(line.split(" ")[0]), float(line.split(" ")[1])
        labels.append(h)
        y.append(w)

except:
    pass


ranks = [b1 for a1,b1 in sorted(list(zip(y,labels)),key=lambda x:x[0])]
ranks = [i+1 for i in range(len(ranks)) if ranks[i]==1]
pos = 0
neg = 0
for i in range(len(labels)):
    if labels[i]==1:
        pos+=1
    else:
        neg+=1


auc = (sum(ranks)-(pos*(pos+1))/2)
auc /= (pos*neg)
print(format(auc,'.2f'))
