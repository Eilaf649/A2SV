class Solution(object):
    
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        odd=n//2
        even=(n+1)//2
        m=(10**9)+7
        return pow(4, odd, m)*pow(5, even, m)%m
           
