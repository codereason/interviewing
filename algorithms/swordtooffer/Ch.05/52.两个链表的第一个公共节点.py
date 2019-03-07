class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if(headA is None or headB is None):
            return None
        cur1,count1 = headA,0
        cur2,count2 = headB,0
        while(cur1 is not None):
            count1+=1
            cur1=cur1.next
        while(cur2 is not None):
            count2+=1
            cur2=cur2.next
        if count1<count2:
            while(count2!=count1):
                headB=headB.next
                count2-=1
            while(headB!=headA):
                headA=headA.next
                headB=headB.next
        else:
            while(count2!=count1):
                headA=headA.next
                count1-=1
            while(headB!=headA):
                headA=headA.next
                headB=headB.next
        return headA
