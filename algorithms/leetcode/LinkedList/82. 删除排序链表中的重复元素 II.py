'''
82. 删除排序链表中的重复元素 II
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。

返回同样按升序排列的结果链表。

 

示例 1：


输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：


输入：head = [1,1,1,2,3]
输出：[2,3]
 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 考察当前的节点时，记住该节点前面的节点；如果该节点是重复的，找到下一个不是该节点的节点，用前面的节点链接；
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            pre = ListNode(float('inf'))
            res = pre
            pre.next = head
            cur = head
            tmp = cur.val
            while cur.next: 
                if cur.next.val!=tmp:
                    pre = cur
                    cur = cur.next
                    tmp = cur.val
                elif cur.next.val==tmp:
                    while cur.next != None and cur.next.val==tmp : 
                        cur = cur.next
                    pre.next = cur.next
                    if cur.next == None:
                        return res.next
                    cur = pre.next
                    tmp = cur.val
            return res.next
        return head

if __name__ == "__main__":
    Node = ListNode
    node1 = Node(1)
    node2 = Node(1)
    node3 = Node(2)
    node4 = Node(3)
    node5 = Node(3)
    node6 = Node(4)
    node7 = Node(4)
    node8 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    print(Solution().deleteDuplicates(node1))
