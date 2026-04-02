# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def isPalindrome(self, head):
        a=[]
        current=head
        while current:
            a.append(current.val)
            current=current.next
        for i in range(len(a)//2):
            if a[i]!=a[len(a)-i-1]:
                return False
        return True
        
