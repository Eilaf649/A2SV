from collections import deque
class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.q=deque()
        self.k=k
        self.value=value

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==self.value:
            self.q.append(num)
        elif self.q:
            while self.q:
                self.q.popleft()
        if num==self.value and len(self.q)>=self.k:
            return True
        else:
            return False
        

        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
