# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removetail(self, head):
        curr=head
        while curr and curr.next and curr.next.next:
            curr=curr.next
        if curr and curr.next:
            y=curr.next.val
            curr.next=None
            return y 
        else:
            return -200
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        count=0
        s=head
        while s:
            s=s.next
            count+=1
        if count!=0:
            k=k%count
            for y in range(k):
                w=self.removetail(head)
                print(w)
                if w!=-200:
                    node=ListNode(w)
                    node.next=head
                    head=node

        return head

        
