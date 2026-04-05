class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
class LRUCache(object):
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def remove(self, node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    def insert(self, node):
        prev=self.head
        nxt=self.head.next
        nxt.prev=node
        prev.next=node
        node.next=nxt
        node.prev=prev

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.cache={}
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru=self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]






#use dict for access


#remove tail[]
#delete element
#swap head
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
