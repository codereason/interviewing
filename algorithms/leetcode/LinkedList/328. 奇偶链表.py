'''
328. 奇偶链表
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
通过次数138,873提交次数212,040
'''
# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head) :
        if head:
            odd = head 
            even = head.next 
            even_head = even
            while  odd.next is not None and even.next is not None: 
                tmp = odd.next.next  ## 取下一个奇数节点
                tmp2 = even.next.next
                odd.next = tmp
                odd = odd.next    #
                even.next = tmp2 
                even = even.next
            odd.next = even_head
        return head


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
    solu = Solution()
    print(solu.oddEvenList(node1))