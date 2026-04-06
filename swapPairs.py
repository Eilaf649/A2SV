# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-1, head)
        prev=dummy
        curr=head
        while curr and curr.next:
            npn=curr.next.next
            second=curr.next
            second.next=curr
            curr.next=npn
            prev.next=second
            prev=curr
            curr=npn
        return (dummy.next)

