class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        count=0
        x=len(piles)
        y=1
        piles.sort(reverse=True)
        while y<x:
            count+=piles[y]
            y+=2
            x-=1
        return count
        
