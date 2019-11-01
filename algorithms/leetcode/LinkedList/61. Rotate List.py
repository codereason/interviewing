# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
61. Rotate List
Medium

758

906

Favorite

Share
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

判断链表长度和k的关系 ==  < >
'''
class Solution:
    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head

        length = self.get_length(head)
        if length < k:
            k = k % length
            return self.rotateRight(head, k)

        if length == k:
            return head

        if length > k:
            steps = length - k + 1
            cur = head
            for i in range(steps - 2):
                cur = cur.next
            end = cur
            cur = cur.next
            new_begin = cur
            while cur.next:
                cur = cur.next
            new_end = cur
            end.next = None
            new_end.next = head
            return new_begin


