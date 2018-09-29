'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: Node
        :rtype: bool
        """
        fast = head
        slow = head
        if head is None: return False
        while (fast.next is not None and fast.next.next is not None):
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False

    def getLoopNode(self, head):

        pass

    def hasCycle2(self, head):
        if head is None: return False
        cur = head
        while head:
            if head.next is cur:
                return True
            next = head.next
            head.next = cur
            head = next
        return False


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    print(Solution().hasCycle(node1))
