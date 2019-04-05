def printLinkedListReverse(root):
    List = []
    if root is not None:
        while(root ):
            List.append(root.val)
            root = root.next
        return List[::-1]

def printLinkedListReverse2(root):
    if root is not None:
        printLinkedListReverse2(root.next)
        print(root.val)

class Node():
    def __init__(self, val):
        self.next = None
        self.val = val
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next=None
    # print(printLinkedListReverse(node1))
    printLinkedListReverse2(node1)