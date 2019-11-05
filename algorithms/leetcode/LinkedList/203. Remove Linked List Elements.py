'''
203. Remove Linked List Elements
Easy

1030

59

Favorite

Share
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.val == val:
            return self.removeElements(head.next,val)
        prev = head
        #设置一个前驱，删除的时候跟踪
        cur = prev.next
        while cur:
            if cur.val == val:
                tmp = cur.next
                prev.next = tmp
                cur = tmp
            else:
                prev= prev.next
                cur = cur.next
        return head