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
#真正有用的方法：分治+merge 两个list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        return self.merge_range_lists(lists, 0, len(lists) - 1)

    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)
        return self.merge_two_lists(left, right)

    def merge_two_lists(self, a, b):
        res = ListNode(0)
        if not a:
            return b
        if not b:
            return a

        if a.val < b.val:
            res.val = a.val
            res.next = self.merge_two_lists(a.next, b)
        else:
            res.val = b.val
            res.next = self.merge_two_lists(a, b.next)
        return res

