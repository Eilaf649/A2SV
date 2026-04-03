# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sumi=ListNode(0)
        curr=sumi
        fst=l1
        snd=l2
        r=0
       
        while l1 or l2 or r:
            if l1:
                x=l1.val
            else:
                x=0
            if l2:
                y=l2.val
            else:
                y=0
            total=(x+y+r)
            r=total//10
            curr.next=ListNode(total%10)
            #print(x)
            #print(sumi)
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            curr=curr.next
        return sumi.next
