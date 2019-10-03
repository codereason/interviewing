N,M = [int(i) for i in input().split()]
class Node:
    def __init__(self,val):
        self.val = val
        self.next=None

res = []
head = Node(1)
tail = head
for i in range(2,N+1):
    tail.next=Node(i)
    tail = tail.next

tail.next = head
while head.next!=head:
    if M>=2:
        for i in range(M-2):
            head = head.next
        res.append(head.next.val)
        head.next = head.next.next

        head=head.next

    else:
        res.append(head.val)
        head.val = head.next.val
        head.next = head.next.next

res.append(head.val)

print(" ".join(str(res[i]) for i in range(len(res))))

