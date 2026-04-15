class StockSpanner(object):

    def __init__(self):
        self.stack=[]
        self.span=1
        self.ans=[]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.ans.append(price)
        #print(self.ans)
        span=1
        while self.stack and price>=self.stack[-1][0]:
            span+=self.stack.pop()[1]
        self.stack.append([price, span])
        return span


        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
