# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        current=head
        n=0
        while current:
            n+=1
            current=current.next
        split_size=n//k
        num_remaining=n%k
        ans=[None]*k
        curr=head
        for i in range(k):
            new_part=ListNode(0)
            tail=new_part
            current_size=split_size
            if num_remaining>0:
                num_remaining-=1
                current_size+=1
            for u in range(current_size):
                tail.next=ListNode(curr.val)
                tail=tail.next
                curr=curr.next
            ans[i]=new_part.next
        return ans
