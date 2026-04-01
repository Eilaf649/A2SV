# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-1, head)
        slow=dummy
        fast=dummy
        for i in range(n+1):
            if fast:
                fast=fast.next
            else:
                return slow.next
        print(fast)
        if fast is None and slow.next is None:
            return None
    
        while fast:
            slow=slow.next
            fast=fast.next
        if slow and slow.next:
            slow.next=slow.next.next
        

        return dummy.next






        """
        current=head
        if current:
            count=0
        while current:
            current=current.next
            count+=1
        dummy=ListNode(-1, head)
        x=count-n
        print(x, count)
        new=dummy.next
        if x==0:
            return head.next
        for i in range(x-1):
            new=new.next
        if new:
            print(new.val)
        if new and new.next:
            new.next=new.next.next
        return dummy.next
        """
            
        
