# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-1, head)
        current=dummy
        for i in range(left-1):
            current=current.next
        c=current.next
        prev=None

        for j in range((right-left)+1):
            nx=c.next
            c.next=prev
            prev=c
            c=nx
        current.next.next=c
        current.next=prev

        return dummy.next
