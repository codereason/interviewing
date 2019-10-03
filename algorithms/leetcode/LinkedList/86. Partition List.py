# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

'''
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None

        left = ListNode("a")
        right = ListNode("a")
        left_cur, right_cur = left, right
        left_list, right_list = [], []
        cur = head
        while cur:
            if cur.val < x:
                left_cur.val = cur.val
                cur = cur.next
                if cur:
                    left_cur.next = ListNode("a")

                left_list.append(left_cur.val)
                left_cur = left_cur.next
            elif cur.val >= x:
                right_cur.val = cur.val
                cur = cur.next
                if cur:
                    right_cur.next = ListNode("a")

                right_list.append(right_cur.val)
                right_cur = right_cur.next
        res = ListNode(-1)
        res_cur = res
        ll = left_list + right_list
        for i in range(len(ll)):
            res_cur.val = ll[i]
            if i != len(ll) - 1:
                res_cur.next = ListNode(-1)
            res_cur = res_cur.next
        return res
#         while left is not None and  left.val!="a":
#             res_cur.val = left.val

#             left=left.next
#             if left:
#                 res_cur.next = ListNode(-1)
#                 res_cur = res_cur.next

#         if right.val =="a":
#             return res

#         while right is not None and right.val!="a":
#             res_cur.val = right.val

#             right=right.next

#             if right is not None and right.val!="a":
#                 res_cur.next = ListNode(-1)
#                 res_cur = res_cur.next

# return res


print("*"*100)

class Solution2(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1 = ListNode(0)
        head2 = ListNode(0)
        cur = head
        p1 = head1
        p2 = head2
        while cur:
            if cur.val < x:
                node = ListNode(cur.val)
                p1.next = node
                p1 = node
            else:
                node = ListNode(cur.val)
                p2.next = node
                p2 = node
            cur = cur.next
        p1.next = head2.next
        return head1.next


