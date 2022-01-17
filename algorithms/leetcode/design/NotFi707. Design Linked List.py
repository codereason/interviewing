'''
707. Design Linked List
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
'''
class Node:
    def __init__(self,val):
        self.val = val #
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def get(self, index: int):
        cur = self.head.next
        while index!=0:
            if cur :
                cur =cur.next
                index-=1
            else:
                return -1
        return cur.val


    def addAtHead(self, val: int) -> None:
        node = Node(val=val)
        node.next = self.head
        self.head = node


    def addAtTail(self, val: int) -> None:
        node =  Node(val=val)
        if not self.tail:
            #移动到尾部
            cur = self.head 
            while cur.next:
                cur = cur.next 
            self.tail = cur
        self.tail.next =node
        node.prev = self.tail
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0: 
            self.addAtHead(val)
            return
        cur = self.head 
        while index!= 0:
            if cur:
                prev = cur
                index-=1 
                cur = cur.next
            else:
                return
        node = Node(val=val)
        prev.next = node
        node.prev = prev
        node.next = cur
        cur.prev = node
        
    def deleteAtIndex(self, index: int) -> None:
        if index == 0: 
            self.head = self.head.next
            self.head.prev = None
            return
        cur = self.head 
        while index!= 0:
            if cur:
                prev = cur
                index-=1 
                cur = cur.next
            else:
                return
        prev.next = cur.next
        cur.next.prev = prev 
        cur.next  = None
        


# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)
myLinkedList.get(1)
myLinkedList.deleteAtIndex(1)
myLinkedList.get(1)
