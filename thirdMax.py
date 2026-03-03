class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=set(nums)
        sn=list(n)
        sn.sort(reverse=True)
        if len(sn)>=3:
            return sn[2]
        else:
            return sn[0]
    
        
