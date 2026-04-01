class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
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
