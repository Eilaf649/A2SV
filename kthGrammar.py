class Solution(object):
    def recurr(self, n,k):
        if n==1:
            return 0
        half=(2**(n-1))//2
        if k>half:
            return 1-self.recurr(n,k-half)
        return self.recurr(n-1,k)

    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        return self.recurr(n,k) 
        
       
