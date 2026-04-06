# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        c=[0]*count
        curr=head
        for i in range(count):
            c[i]+=curr.val
            curr=curr.next
        rev=head
        prev=None
        while rev:
            nex=rev.next
            rev.next=prev
            prev=rev
            rev= nex
        #print(prev)
        t=prev
        maxi=float("-inf")
        for i in range(count):
            c[i]+=t.val
            t=t.next
        maxi=max(c)
        c.sort(reverse=True)
        #print(c)
        return c[0]
        
