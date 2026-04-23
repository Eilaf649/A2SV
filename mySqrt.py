class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left=0
        right=x
        if x==0 or x==1:
            return x
        while right>=left:
            
            mid=(right+left)//2
            print(mid, left, right)
            if mid**2==x:
                return mid
            elif mid**2<x:
                left=mid+1
            else:
                right=mid-1
        return(left-1)
