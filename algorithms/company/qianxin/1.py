highet = int(input())
l = list(map(int,input().split(" ")))
pair = input()
p,q=int(pair.split(" ")[0]),int(pair.split(" ")[1])




from collections import deque
class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left,self.right=None,None

def deserize(data):
    if not data or data[0]==-1:return None
    q = deque()
    root = TreeNode(int(data[0]))
    q.append(root)
    i = 1
    while q and i < len(data):
        n = q.popleft()
        if data[i]!=-1:
            n.left=TreeNode(int(data[i]))
            q.append(n.left)
        i+=1
        if data[i] !=-1:
            n.right = TreeNode(data[i])
            q.append(n.right)
        i+=1
    return root

def find_recent_ancestors(root,p,q):
    if root is None:
        return None
    if min(p,q)<=root.val<=max(p,q):
        return root
    else:
        l=find_recent_ancestors(root.left,p,q)
        r = find_recent_ancestors(root.right,p,q)
        if l:
            return l
        if r:
            return r


def find_recent_ancestors1(root,p,q):
    if root is None:
        return None
    while(root!=None):
        if p>root.val and q>root.val:
            root=root.right
        elif p<root.val and q<root.val:
            root=root.left
        else:
            return root


tree = deserize(l)

aa = find_recent_ancestors1(tree,p,q)
if aa is None:print(-1)
else:
    print(aa.val)
