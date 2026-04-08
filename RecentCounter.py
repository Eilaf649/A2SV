from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.q= deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        
        self.q.append(t)
        if self.q and t-3000>self.q[0]:
            self.q.popleft()
        print(self.q)
        return len(self.q)



        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
