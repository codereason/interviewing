'''
Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
一种方法是：从末尾删去第n个相当于从头删去第L-n+1个，此出不再赘述
'''


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pt1 = head
        pt2 = head
        for _ in range(n):
            pt1 = pt1.next
        if pt1 is None: return head.next
        while pt1.next:
            pt1 = pt1.next
            pt2 = pt2.next
        pt2.next = pt2.next.next
        return head
