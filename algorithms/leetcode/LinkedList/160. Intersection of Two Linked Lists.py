'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.


方法：先确定两个链表的长度，将较长的链表截掉较长的那一部分lenA - lenB，这样子两个链表长度相等，即可while比较
'''


# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA is None or headB is None):
            return None
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        if (lenA > lenB):
            while (lenA != lenB):
                headA = headA.next
                lenA -= 1
        if (lenA < lenB):
            while (lenA != lenB):
                headB = headB.next
                lenB -= 1
        while (headA != headB):
            headA = headA.next
            headB = headB.next
        return headA

    def getLength(self, head):
        count = 0
        while (head != None):
            count += 1
            head = head.next
        return count

# if __name__ == "__main__":
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     node5 = Node(5)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#     node5.next = node2
#     print(Solution().hasCycle(node1))
