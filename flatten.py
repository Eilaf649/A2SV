"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        current=head
        while current:
            if current.child:
                nxt=current.next
                a=current.child
                a.prev=current
                current.next=a
                while a and a.next!=None:
                    a=a.next
                if nxt:
                    nxt.prev=a
                if a:
                    a.next=nxt
                current.child=None
            current=current.next
        print(head)
        return head
