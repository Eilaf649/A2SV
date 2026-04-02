# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def isPalindrome(self, head):
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        #if fast:
            #slow=slow.next
        prev=None
        current=slow
        while slow:
            nex=slow.next
            slow.next=prev
            prev=slow
            slow=nex
        fast=head
        slow=prev
        while slow:
            if slow.val!=fast.val:
                return False
            fast=fast.next
            slow=slow.next
        return True
        







        """
        a=[]
        current=head
        while current:
            a.append(current.val)
            current=current.next
        for i in range(len(a)//2):
            if a[i]!=a[len(a)-i-1]:
                return False
        return True
        """
