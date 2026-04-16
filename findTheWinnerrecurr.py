class Solution(object):
    def recurr(self, friends, i):
        if len(friends)==1:
            return friends[0]
        i=(i+self.k-1) % len(friends)
        friends.pop(i)
        return self.recurr(friends, i)
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        self.k=k
        friends=[i for i in range(1,n+1)]
        return self.recurr(friends, 0)

