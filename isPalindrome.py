class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        x=list(x)
        start=0
        end= len(x)-1
        while end>=start:
            if x[end]!=x[start]:
                return False
            end-=1
            start+=1
        return True
        
