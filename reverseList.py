# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current=head
        prev=None
        while current:
            nex=current.next
            current.next=prev
            prev=current
            current=nex
        return prev

            

        
       
        
        
