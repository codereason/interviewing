'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         if l1 is None:return l2
#         if l2 is None:return l1
#         str1,str2 = self.getNumbers(l1),self.getNumbers(l2)
#         # print(str1,str2)
#         sums = int(str1)+int(str2)
#         List = list(str(sums))
#         print(List)

#         cur = ListNode(List[-1])
#         res = cur
#         for i in range(2,len(List)+1):
#             cur.next = ListNode(List[-1*i])

#             cur = cur.next
#         return res



#     def getNumbers(self,node):
#         if node is None:return [0]
#         else:
#             str1 = ''
#             while node:
#                 str1 += str(node.val)
#                 node = node.next
#             return str1[::-1]

class Solution:
    def addTwoNumbers(self, l1, l2):
        '''
        一个非常cheap的解法，纠结于进位。
        另外一个方法是把两个链表的数拉出来变成整数再相加，
        结果再转换成链表返回的方法要简单很多，不用纠结进位
        '''
        # if l1 is None:return l2
        # if l2 is None:return l1
        cur = ListNode(0)
        res = cur
        flag = 0
        while((l1 or l2)):
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            cur.val = l1val + l2val + cur.val
            # print(l1val,l2val,cur.val)
            flag = 0
            if cur.val >= 10:

                flag = 1
                cur.val-=10

            if flag == 1 :
                cur.next= ListNode(1)
            else:cur.next = ListNode(0)
            tail = cur
            cur = cur.next

            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None
        if cur.val == 0:  ##如果两个三位数相加还是三位数会出现尾巴，如[7,0,8,0]，这个tail尾指针就是指向实际最高那一位并把多余的0位
                          ##去掉
            tail.next = None

        return res
    # def getLength(self,node):
    #     count = 0
    #     if node is None:return 0
    #     else:
    #         while(node):
    #             count+=1
    #             node = node.next
    #         return count