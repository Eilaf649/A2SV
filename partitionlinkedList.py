# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def add(self, head, val):
        node=ListNode(val)
        current=head
        while current.next:
            current=current.next
        current.next=node
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-1, head)
        left=ListNode(-1, None)
        right= ListNode(-1, None)
        current=dummy.next
        while current:
            if current and current.val>=x:
                c=current.val
                self.add(right, c)
                #rint(c, right)
            elif  current and current.val<x:
                c=current.val
                print(c, left)
                self.add(left, c)
            current=current.next
        a=left
        while a.next:
            a=a.next
        a.next=right.next
        return left.next
