'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
Accepted
465,173
Submissions
1,278,619
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        length = len(lists)

        cur = ListNode(-1)
        res = cur
        ll = []
        for i in range(length):
            tmp = lists[i]

            while tmp:
                ll.append(tmp.val)
                tmp = tmp.next
        print(ll)
        ll.sort()
        if len(ll) == 0: return None
        for i in range(len(ll)):
            cur.val = ll[i]
            if i != len(ll) - 1:
                cur.next = ListNode(-1)
                cur = cur.next
        return res